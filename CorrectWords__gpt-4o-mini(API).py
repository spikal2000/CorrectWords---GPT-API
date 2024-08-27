# -*- coding: utf-8 -*-
"""
Created on Sat Aug 24 08:10:11 2024

@author: spika
"""
# from openai import OpenAI


# client = OpenAI()

# completion = client.chat.completions.create(
#     model="gpt-4o-mini",
#     messages=[
#         {"role": "system", "content": "You are a helpful assistant."},
#         {
#             "role": "user",
#             "content": "tell me a joke"
#         }
#     ]
# )

# print(completion.choices[0].message.content)


# Actual Code 
from openai import OpenAI
import pandas as pd
import mysql.connector
from mysql.connector import Error
import time
import re

client = OpenAI()

# Read CSV file
file_path = 'wholesalers.csv'

# Read the CSV file with a semicolon delimiter
correct_names_df = pd.read_csv(file_path, delimiter=';')

# Keep only the first and second columns
correct_names_df = correct_names_df.iloc[:, :2]

# Prepare the prompt for GPT that includes the pre-processed dictionary
base_prompt = (
    "You have a list of correctly spelled wholesaler names and their corresponding descriptions, along with a list of misspelled wholesaler names. "
    "Your task is to match each misspelled name to its correct counterpart based on either the wholesaler name or description. "
    "Ensure that similar names are matched consistently, regardless of slight variations. "
    "If no suitable match exists or the input is blank, return only 'idk'. "
    "Here is the list of correct wholesaler names and descriptions:\n"
    f"{correct_names_df.to_string(index=False)}\n"
    "Please provide only the matched wholesaler name:"
)

def normalize_name(name):
    """Normalize the input name by trimming spaces, lowering case, and removing special characters."""
    return re.sub(r'\s+', ' ', name.strip().lower())

def batch_get_completion_with_retry(names, retries=3, delay=5):
    """Function to get completions for a batch of names from the GPT-4o-mini API with retry logic."""
    normalized_names = [normalize_name(name) for name in names]
    names_str = "\n".join([f"{i+1}. {name}" for i, name in enumerate(normalized_names)])
    prompt = f"{base_prompt}\nThe names to match are:\n{names_str}"

    for attempt in range(retries):
        try:
            completion = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {"role": "system", "content": "You are a helpful assistant."},
                    {"role": "user", "content": prompt}
                ]
            )
            # Assume the model returns a list of names separated by line breaks
            corrected_names = completion.choices[0].message.content.strip().split("\n")
            processed_names = [name.strip().split(". ")[-1] for name in corrected_names]
            return processed_names
        except Exception as e:
            print(f"Attempt {attempt + 1} failed with error: {e}")
            if attempt < retries - 1:
                time.sleep(delay)
            else:
                raise e

try:
    connection = mysql.connector.connect(
        host='84.254.29.206',
        user='admin',
        password='Vaggosspyros!997',
        database='kalogeris_portal'
    )

    if connection.is_connected():
        cursor = connection.cursor(dictionary=True)

        # Fetch distinct names
        cursor.execute("SELECT DISTINCT name FROM kalogeris_portal.dataExpenses WHERE corrected_name IS NULL")
        rows = cursor.fetchall()

        # Group rows into batches
        batch_size = 10
        for i in range(0, len(rows), batch_size):
            batch_rows = rows[i:i + batch_size]
            names = [row['name'] for row in batch_rows]

            try:
                # Get corrections for the batch
                corrected_names = batch_get_completion_with_retry(names)

                # Update MySQL with the corrected names or 'idk'
                for row, corrected_name in zip(batch_rows, corrected_names):
                    update_query = "UPDATE kalogeris_portal.dataExpenses SET corrected_name = %s WHERE name = %s"
                    cursor.execute(update_query, (corrected_name, row['name']))
                    connection.commit()

            except Exception as e:
                print(f"Failed to process batch starting with {names[0]} after multiple attempts: {e}")

except Error as e:
    print(f"MySQL Error: {e}")
finally:
    if 'connection' in locals() and connection.is_connected():
        cursor.close()
        connection.close()





            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            