import pandas as pd

# Original data (used for testing and later combined with custom data)
df = pd.DataFrame({
    'raw_name': [
        "CAPPUCCINO  FREDDO  PREMIUM", "CAPPUCCINO  ΔΙΠΛΟΣ  PREMIUM", "CAPPUCCINO ΜΟΝΟ  PREMIUM", 
        "COCA COCA  LIGHT", "COCA-COLA", "COOKIES ΣΟΚΟΛΑΤΑΣ", "DOMINO", "DONUTS", 
        "ESPRESSO   ΔΙΠΛΟΣ  PREMIUM", "Fanta μπλε", "JACOBS", "Jubo clasic Χωρις γλουτενη", 
        "LIFE  APPLE  ORANGE  CARROT", "LURPAK ΒΟΥΤΥΡΟ", "MILKO", "MILKO FREE", "MOTION", 
        "NESCAFE", "PANNETONE TEMAXIO", "Soda", "TOΥΡΤΕΣ ΤΟ ΚΙΛΟ", "XOΡΙΑΤΙΚΟ  ΠΡΟΖΥΜΙ", 
        "ZERO", "amstel", "choco flakes τραγανες νιφαδες", "green cola", "ice green λεμονι", 
        "ΑΜΥΓΔΑΛΟΥ", "ΒΑΣΙΛΟΠΙΤΑ ΤΣΟΥΡΕΚΙ", "ΒΙΟΛ ΚΑΤΣΙΚΙΣΙΟ", "ΒΙΟΛΟΓΙΚΑ ΑΥΑ", 
        "Βιολογικη σοδεια λεμονι", "Βλαχας γαλα", "ΓΑΛΑ ΔΕΛΤΑ ΠΡΑΣΙΝΟ", "ΓΑΛΑΚΤΟΜΠΟΥΡΕΚΟ  ΚΟΜΜΑΤΙ", 
        "ΓΑΛΑΚΤΟΜΠΟΥΡΕΚΟ ΜΑΙΣΕΟ", "ΓΑΛΑΤΟΠΙΤΑ ΚΟΜΑΤΙ", "ΓΑΛΛΙΚΟΣ", "ΓΕΡΜΑΝΙΚΟ  ΚΙΛΟ", 
        "ΔΙΠΛΕΣ", "ΕSPRESSO FREDDO  PREMIUM", "ΖΑΜΠΟΝΟΤΥΡΟΠΙΤΑ", "ΚΑΛΑΜΠΟΚΙ ΦΡΑΤΖΟΛΑ", 
        "ΚΑΛΤΣΟΝΕ ΚΟΤΟΠΟΥΛΟ", "ΚΑΣΕΡΟΠΙΤΑ", "ΚΑΤΣΙΚΙΣΙΟ ΜΕΒΓΑΛ ΓΙΑΟΥΡΤΙ", 
        "ΚΕΙΚ ΒΑΣΙΛΟΠΙΤΑ", "ΚΟΛΟΚΥΘΟΠΙΤΑ ΚΟΜΜΑΤΙ", "ΚΟΡΜΟΣ ΧΡΙΣΤΟΥΓΕΝΙΑΤΙΚΟΣ", 
        "ΚΟΥΛ ΓΑΛΟΠ ΦΙΛΑΔΕΛΦ", "ΚΟΥΛΟΥΡΙ  ΘΕΣΣΑΛΟΝΙΚΗΣ", "ΚΟΥΛΟΥΡΙ ΗΛΙΟΣΠΟΡΟ", 
        "ΚΡΙΤΣΙΝΙΑ ΖΕΑΣ", "ΚΡΙΤΣΙΝΙΑ ΜΕ ΕΛΙΑ", "ΚΡΙΤΣΙΝΙΑ ΣΤΑΡΕΝΙΑ", "ΚΡΙΤΣΙΝΙΑ ΤΥΡΙ", 
        "ΚΡΟΥΑΣΑΝ ΒΟΥΤΗΡΟΥ", "ΚΡΟΥΑΣΑΝ ΒΟΥΤΥΡΟΥ", "ΚΡΟΥΑΣΑΝ ΒΟΥΤΥΡΟΥ ΜΕΣΑΙΟ", 
        "ΚΡΟΥΑΣΑΝ ΖΑΜΠΟΝ ΤΥΡΙ", "ΚΡΟΥΑΣΑΝ ΣΟΚΟΛΑΤΑΣ", "ΚΩΚΑΚΙΑ", "ΛΑΔΟΨΩΜΟ", 
        "ΛΟΥΚΑΝΙΚΟΠΙΤΑΚΙΑ", "ΛΟΥΚΟΥΜΑΔΑΚΙ", "ΛΟΥΚΟΥΜΑΣ", "ΜΑΡΓΑΡΙΤΑ", 
        "ΜΑΥΡΟ ΠΕΤΡΙΤΗΣ ΕΡΥΘΡΟΣ", "ΜΕΒΓΑΛ ΕΛΑΦΡΥ", "ΜΕΒΓΑΛ ΠΛΗΡΕΣ", 
        "ΜΕΛΟΜΑΚΑΡΟΝΑ ΜΠΟΥΚΙΤΣΕΣ ΚΑΙ ΚΟΥΡΑΜΠΙΕΔΕΣ", "ΜΗΛΟΠΙΤΑ  ΜΕΓΑΛΗ", "ΜΗΛΟΠΙΤΑ  ΜΕΣΑΙΑ", 
        "ΜΗΛΟΠΙΤΑ ΜΙΚΡΗ", "ΜΟΥΣΤΑΛΕΥΡΙΑ", "ΜΟΥΣΤΟΚΟΥΛΟΥΡΑ ΤΡΑΓΑΝΑ  ΜΑΛΑΚΑ", 
        "ΜΠΑΓΚΕΤΑ ΧΩΡΙΑΤ", "ΜΠΑΚΛΑΒΑΣ ΚΟΜΜΑΤΙ", "ΜΠΙΣΚΟΤΟ ΚΟΡΜΟΣ", "ΜΠΟΥΓΑΤΣΑ ΓΛΥΚΙΑ", 
        "ΜΠΡΙΟΣ", "ΝΕΓΡΑΚΙΑ", "ΝΕΡΟ ΜΙΚΡΟ", "ΠΑΣΤΕΣ ΤΕΜΑΧΙΟ", "ΠΕΙΝΙΡΛΑΚΙΑ", 
        "ΠΕΙΝΙΡΛΙ Ζαμπον τυρι", "ΠΕΙΝΙΡΛΙ ΜΕ ΛΟΥΚΑΝΙΚΟ", "ΠΙΡΟΣΚΑΚΙΑ", "ΠΙΤΣΑ", 
        "ΠΟΛΥΣΠΟΡΟ", "ΠΟΛΥΤΕΛΕΙΑΣ", "ΠΟΡΤΟΚΑΛΟΠΙΤΑ", "ΠΟΡΤΟΚΑΛΟΠΙΤΑ ΤΑΨΑΚΙ ΜΙΚΡΟ", 
        "ΠΡΟΖΥΜΙ ΜΙΣΟ ΚΙΛΟ", "ΠΡΟΣΦΟΡΟ  ΜΙΚΡΟ", "ΠΡΟΦΙΤΕΡΟΛ  ΜΕΣΑΙΟ", "ΠΡΟΦΙΤΕΡΟΛ ΜΕΓΑΛΟ", 
        "ΣΟΚΟΛΑΤΑ", "ΣΟΚΟΛΑΤΟΠΙΤΑ ΚΟΜΜΑΤΙ", "ΣΠΑΝΑΚΟΠΙΤΑ ΤΑΨΙΟΥ", "ΣΠΑΝΑΚΟΠΙΤΑ ΤΡΙΓΩΝΗ", 
        "ΤΑΡΤΑΚΙΑ ΔΙΑΦΟΡΑ  ΛΕΜΟΝΟΠΙΤΑΚΙΑ", "ΤΟΣΤ ΜΑΥΡΟ", "ΤΣΑΙ", "ΤΣΟΥΡΕΚΑΚΙ ΣΙΡΟΠΙΑΣΤΟ ΜΕΓΑΛΟ", 
        "ΤΥΛΙΧΤΑ ΔΙΑΦΟΡΑ", "ΤΥΡΟΠΙΤΑ ΣΦΟΛΙΑΤΑΣ", "ΤΥΡΟΠΙΤΑ ΤΑΨΙΟΥ", "ΤΥΡΟΠΙΤΑΚΙΑ", 
        "ΦΑΓΕ ΤΡΙΜΜΕΝΟ ΤΥΡΙ GOUDA", "ΦΑΓΗΤΑ", "ΦΡΑΠΕ", "ΦΡΑΤΖΟΛΑΚΙΑ ΣΤΡΟΓΓΙΛΑ", 
        "ΧΡΙΣΤΟΚΟΥΛΟΥΡΕΣ", "ΧΩΡΙΑΤΙΚΟ  ΜΙΚΡΟ", "ΨΩΜΙ ΠΡΟΖ ΟΛΙΚΗΣ ΛΕΥΚΟ", "Ψωμί της Γιαγιάς"
    ],
    'standardized_name': [
        "Cappuccino Freddo Premium", "Cappuccino Διπλός Premium", "Cappuccino Μονό Premium", 
        "Coca-Cola Light", "Coca-Cola", "Cookies Σοκολάτας", "Domino", "Donuts", 
        "Espresso Διπλός Premium", "Fanta Μπλε", "Jacobs", "Jumbo Classic Χωρίς Γλουτένη", 
        "Life Apple Orange Carrot", "Lurpak Βούτυρο", "Milko", "Milko Free", "Motion", 
        "Nescafe", "Panettone Τεμάχιο", "Soda", "Τούρτες Το Κιλό", "Χωριάτικο Προζύμι", 
        "Zero", "Amstel", "Choco Flakes Τραγανές Νιφάδες", "Green Cola", "Ice Green Λεμόνι", 
        "Αμυγδάλου", "Βασιλόπιτα Τσουρέκι", "Βιολ Κατσικίσιο", "Βιολογικά Αυγά", 
        "Βιολογική Σοδειά Λεμόνι", "Βλάχας Γάλα", "Γάλα Δέλτα Πράσινο", "Γαλακτομπούρεκο Κομμάτι", 
        "Γαλακτομπούρεκο Μέσο", "Γαλατόπιτα Κομμάτι", "Γαλλικός", "Γερμανικό Κιλό", 
        "Δίπλες", "Espresso Freddo Premium", "Ζαμπονοτυρόπιτα", "Καλαμπόκι Φραντζόλα", 
        "Καλτσόνε Κοτόπουλο", "Κασερόπιτα", "Κατσικίσιο Μεβγάλ Γιαούρτι", 
        "Κέικ Βασιλόπιτα", "Κολοκυθόπιτα Κομμάτι", "Κορμός Χριστουγεννιάτικος", 
        "Κούλουρι Γαλοπούλα Φιλαδέλφεια", "Κουλούρι Θεσσαλονίκης", "Κουλούρι Ηλιόσπορο", 
        "Κριτσίνια Ζέας", "Κριτσίνια με Ελιά", "Κριτσίνια Σταρένια", "Κριτσίνια Τυρί", 
        "Κρουασάν Βουτύρου", "Κρουασάν Βουτύρου", "Κρουασάν Βουτύρου Μεσαίο", 
        "Κρουασάν Ζαμπόν Τυρί", "Κρουασάν Σοκολάτας", "Κωκάκια", "Λαδόψωμο", 
        "Λουκανικοπιτάκια", "Λουκουμαδάκι", "Λουκουμάς", "Μαργαρίτα", 
        "Μαύρο Πετρίτης Ερυθρός", "Μεβγάλ Ελαφρύ", "Μεβγάλ Πλήρες", 
        "Μελομακάρονα Μπουκίτσες και Κουραμπιέδες", "Μηλόπιτα Μεγάλη", "Μηλόπιτα Μεσαία", 
        "Μηλόπιτα Μικρή", "Μουσταλευριά", "Μουστοκούλουρα Τραγανά Μαλακά", 
        "Μπαγκέτα Χωριάτικη", "Μπακλαβάς Κομμάτι", "Μπισκότο Κορμός", "Μπουγάτσα Γλυκιά", 
        "Μπριός", "Νεγράκια", "Νερό Μικρό", "Πάστες Τεμάχιο", "Πεϊνιρλάκια", 
        "Πεϊνιρλί Ζαμπόν Τυρί", "Πεϊνιρλί με Λουκάνικο", "Πιροσκάκια", "Πίτσα", 
        "Πολύσπορο", "Πολυτέλειας", "Πορτοκαλόπιτα", "Πορτοκαλόπιτα Ταψάκι Μικρό", 
        "Προζύμι Μισό Κιλό", "Πρόσφορο Μικρό", "Προφιτερόλ Μεσαίο", "Προφιτερόλ Μεγάλο", 
        "Σοκολάτα", "Σοκολατόπιτα Κομμάτι", "Σπανακόπιτα Ταψιού", "Σπανακόπιτα Τριγωνή", 
        "Ταρτάκια Διάφορα Λεμονόπιτακια", "Τοστ Μαύρο", "Τσάι", "Τσουρεκάκι Σιροπιαστό Μεγάλο", 
        "Τυλιχτά Διάφορα", "Τυρόπιτα Σφολιάτας", "Τυρόπιτα Ταψιού", "Τυροπιτάκια", 
        "Φάγε Τριμμένο Τυρί Gouda", "Φαγητά", "Φραπέ", "Φραντζολάκια Στρογγυλά", 
        "Χριστοκούλουρες", "Χωριάτικο Μικρό", "Ψωμί Προζύμι Ολικής Λευκό", "Ψωμί της Γιαγιάς"
    ]
})

custom_data = {
    "Cappuccino Freddo Premium": ["CAPPUCCINO FREDDO", "CAPPUCCINO PREMIO FREDDO", "CAPPUCCINO FREDDO PREM"],
    "Cappuccino Διπλός Premium": ["CAPPUCCINO ΔΙΠΛΟΣ", "CAPPUCCINO DOUBLE", "CAPPUCCINO ΔΙΠΛΟ ΠΡΕΜΙΟΥΜ"],
    "Cappuccino Μονό Premium": ["CAPPUCCINO ΜΟΝΟ", "CAPPUCCINO SINGLE", "CAPPUCCINO ΜΟΝΟ ΠΡΕΜΙΟΥΜ"],
    "Coca-Cola Light": ["COCA COLA LIGHT", "COCA-LIGHT", "COCA LIGHT"],
    "Coca-Cola": ["COKE", "COCA COLA", "COCA-COLA REGULAR"],
    "Cookies Σοκολάτας": ["COOKIE ΣΟΚΟΛΑΤΑΣ", "COOKIES ΣΟΚΟΛΑΤΕΣ", "COOKIES CHOCOLATE"],
    "Domino": ["DOMINO BISCUIT", "DOMINOS", "DOMINOES"],
    "Donuts": ["DONUT", "DOUGHNUT", "DONUTS CLASSIC"],
    "Espresso Διπλός Premium": ["ESPRESSO DOUBLE PREMIUM", "ESPRESSO ΔΙΠΛΟ", "ESPRESSO ΔΙΠΛΟΣ ΠΡΕΜΙΟΥΜ"],
    "Fanta Μπλε": ["FANTA BLUE", "ΦΑΝΤΑ ΜΠΛΕ", "FANTA ΜΠΛΟΥ"],
    "Jacobs": ["JACOBS COFFEE", "JACOBS PREMIUM", "JACOBS INSTANT"],
    "Jumbo Classic Χωρίς Γλουτένη": ["JUMBO GLUTEN FREE", "JUMBO CLASSIC NO GLUTEN", "JUMBO ΧΩΡΙΣ ΓΛΟΥΤΕΝΗ"],
    "Life Apple Orange Carrot": ["LIFE JUICE", "APPLE ORANGE CARROT", "LIFE ΑΠΟΛΟΚΑΡΟΤΟ"],
    "Lurpak Βούτυρο": ["LURPAK BUTTER", "LURPAK ΒΟΥΤΥΡΟ", "LURPAK ΒΟΥΤΙΡΟ"],
    "Milko": ["MILCO", "MILKO DRINK", "MILK O"],
    "Milko Free": ["MILKO SUGAR FREE", "MILKO ΧΩΡΙΣ ΖΑΧΑΡΗ", "MILKO FREE DRINK"],
    "Motion": ["MOTION ENERGY", "MOTION DRINK", "MOTION BEVERAGE"],
    "Nescafe": ["NESCAFE CLASSIC", "NESCAFE COFFEE", "NESCAFE INSTANT"],
    "Panettone Τεμάχιο": ["PANETTONE PIECE", "PANETONE SLICE", "ΠΑΝΕΤΟΝΕ ΤΕΜ"],
    "Soda": ["SODA WATER", "SODA DRINK", "ΣΟΔΑ"],
    "Τούρτες Το Κιλό": ["ΤΟΥΡΤΕΣ ΚΙΛΟ", "CAKES PER KILO", "TOURTES KILO"],
    "Χωριάτικο Προζύμι": ["ΧΩΡΙΑΤΙΚΟ ΨΩΜΙ", "VILLAGE BREAD", "PROZYMI ΧΩΡΙΑΤΙΚΟ"],
    "Zero": ["ZERO DRINK", "ZERO CALORIE", "ZERO COKE"],
    "Amstel": ["AMSTEL BEER", "AMSTEL BREW", "AMSTEL LAGER"],
    "Choco Flakes Τραγανές Νιφάδες": ["CHOCO FLAKES", "TRAΓΑΝΕΣ ΝΙΦΑΔΕΣ", "CHOCOLATE FLAKES"],
    "Green Cola": ["GREEN-COLA", "GRN COLA", "COLA GREEN"],
    "Ice Green Λεμόνι": ["ICE GREEN LEMON", "ΛΕΜΟΝΙ ICE GREEN", "ICE ΛΕΜΟΝΙ"],
    "Αμυγδάλου": ["ΑΜΥΓΔΑΛΟΥ ΠΑΓΩΤΟ", "ALMOND ICE CREAM", "ALMOND DESSERT"],
    "Βασιλόπιτα Τσουρέκι": ["ΒΑΣΙΛΟΠΙΤΑ ΤΣΟΥΡΕΚΙ", "BASILO TSOURAKI", "BASILO CAKE"],
    "Βιολ Κατσικίσιο": ["ΒΙΟΛ ΚΑΤΣΙΚΙΣΙΟ", "GOAT MILK", "VIOL GOAT"],
    "Βιολογικά Αυγά": ["BIOLOGIKA AVGA", "ΒΙΟ ΑΥΓΑ", "BIO EGGS"],
    "Βιολογική Σοδειά Λεμόνι": ["ΒΙΟΛ ΣΟΔΕΙΑ ΛΕΜΟΝΙ", "BIO LEMON JUICE", "BIO ΣΟΔΕΙΑ"],
    "Βλάχας Γάλα": ["ΒΛΑΧΑΣ ΓΑΛΑ", "VLAXA MILK", "VLAXAS MILK"],
    "Γάλα Δέλτα Πράσινο": ["ΔΕΛΤΑ ΠΡΑΣΙΝΟ ΓΑΛΑ", "DELTA GREEN MILK", "GALA ΠΡΑΣΙΝΟ"],
    "Γαλακτομπούρεκο Κομμάτι": ["ΓΑΛΑΚΤΟΜΠΟΥΡΕΚΟ ΠΙΤΑ", "GALAKTO PIECE", "ΓΑΛΑΚΤΟ ΜΠΟΥΡΕΚΟ"],
    "Γαλακτομπούρεκο Μέσο": ["ΓΑΛΑΚΤΟΜΠΟΥΡΕΚΟ", "GALAKTO BOURIKO", "ΓΑΛΑΚΤΟ ΜΕΣΑΙΟ"],
    "Γαλατόπιτα Κομμάτι": ["ΓΑΛΑΤΟΠΙΤΑ ΚΟΜΜΑΤΙ", "GALA PIECE", "ΓΑΛΑΤΟΠΙΤΑ"],
    "Γαλλικός": ["ΓΑΛΛΙΚΟΣ ΚΑΦΕΣ", "FRENCH COFFEE", "FRENCH KAFES"],
    "Γερμανικό Κιλό": ["ΓΕΡΜΑΝΙΚΟ ΚΙΛΟ", "GERMAN KILO", "GERMAN BREAD"],
    "Δίπλες": ["ΔΙΠΛΕΣ DESSERT", "DIPLES", "DIPLES PASTRY"],
    "Espresso Freddo Premium": ["ESPRESSO FREDDO", "FREDDO ESPRESSO", "ESPRESO ΠΡΕΜΙΟΥΜ"],
    "Ζαμπονοτυρόπιτα": ["ΖΑΜΠΟΝΟΤΥΡΟ ΠΙΤΑ", "HAM & CHEESE PIE", "ΖΑΜΠΟΝ ΠΙΤΑ"],
    "Καλαμπόκι Φραντζόλα": ["ΚΑΛΑΜΠΟΚΙ ΨΩΜΙ", "CORN BREAD", "ΚΑΛΑΜΠΟΚΙ ΦΡΑΝΤΖΟΛΑ"],
    "Καλτσόνε Κοτόπουλο": ["ΚΑΛΤΣΟΝΕ ΚΟΤΟ", "CALZONE CHICKEN", "ΚΑΛΤΣΟΝΕ ΚΟΤΟΠΟΥΛΟ"],
    "Κασερόπιτα": ["ΚΑΣΕΡΟ ΠΙΤΑ", "KASERO PIE", "CHEESE PIE"],
    "Κατσικίσιο Μεβγάλ Γιαούρτι": ["ΚΑΤΣΙΚΙΣΙΟ ΓΙΑΟΥΡΤΙ", "GOAT YOGHURT", "ΜΕΒΓΑΛ YOGURT"],
    "Κέικ Βασιλόπιτα": ["ΚΕΙΚ ΒΑΣΙΛΟΠΙΤΑ", "BASILO CAKE", "BASILOPITA KEIK"],
    "Κολοκυθόπιτα Κομμάτι": ["ΚΟΛΟΚΥΘΟΠΙΤΑ PIECE", "PUMPKIN PIE", "ΚΟΛΟΚΥΘΟ ΠΙΤΑ"],
    "Κορμός Χριστουγεννιάτικος": ["ΚΟΡΜΟΣ ΧΡΙΣΤ", "XMAS YULE LOG", "CHRISTMAS LOG"],
    "Κούλουρι Γαλοπούλα Φιλαδέλφεια": ["ΚΟΥΛΟΥΡΙ ΓΑΛΟΠΟΥΛΑ", "TURKEY KULURI", "KULOURI ΦΙΛΑΔΕΛΦΕΙΑ"],
    "Κουλούρι Θεσσαλονίκης": ["ΚΟΥΛΟΥΡΙ ΘΕΣΣ", "THESS KULOURI", "THESSALONIKI BREAD"],
    "Κουλούρι Ηλιόσπορο": ["ΚΟΥΛΟΥΡΙ ΗΛΙΟΣΠΟΡΟ", "SUNFLOWER KULOURI", "ΗΛΙΟΣΠΟΡΟ ΚΟΥΛΟΥΡΙ"],
    "Κριτσίνια Ζέας": ["ΚΡΙΤΣΙΝΙΑ ΖΕΑΣ", "ZEAS BREADSTICKS", "ΖΕΑΣ ΚΡΙΤΣΙΝΙΑ"],
    "Κριτσίνια με Ελιά": ["ΚΡΙΤΣΙΝΙΑ ΕΛΙΑΣ", "OLIVE BREADSTICKS", "ΚΡΙΤΣΙΝΙΑ ΕΛΙΕΣ"],
    "Κριτσίνια Σταρένια": ["ΚΡΙΤΣΙΝΙΑ ΣΤΑΡΕΝΙΑ", "WHEAT BREADSTICKS", "ΣΤΑΡΕΝΙΑ ΚΡΙΤΣΙΝΙΑ"],
    "Κριτσίνια Τυρί": ["ΚΡΙΤΣΙΝΙΑ ΤΥΡΙ", "CHEESE BREADSTICKS", "ΤΥΡΙ ΚΡΙΤΣΙΝΙΑ"],
    "Κρουασάν Βουτύρου": ["ΚΡΟΥΑΣΑΝ ΒΟΥΤΥΡΟΥ", "BUTTER CROISSANT", "ΚΡΟΥΑΣΑΝ ΒΟΥΤΙΡΟ"],
    "Κρουασάν Βουτύρου Μεσαίο": ["ΚΡΟΥΑΣΑΝ ΜΕΣΑΙΟ", "MEDIUM CROISSANT", "CROISSANT ΜΕΣΑΙΟ"],
    "Κρουασάν Ζαμπόν Τυρί": ["ΚΡΟΥΑΣΑΝ ΖΑΜΠΟΝ", "HAM & CHEESE CROISSANT", "ΚΡΟΥΑΣΑΝ ΤΥΡΙ"],
    "Κρουασάν Σοκολάτας": ["ΚΡΟΥΑΣΑΝ ΣΟΚΟΛΑΤΑΣ", "CHOCOLATE CROISSANT", "ΣΟΚΟΛΑΤΑ ΚΡΟΥΑΣΑΝ"],
    "Κωκάκια": ["ΚΩΚΑΚΙΑ DESSERT", "KOCAKIA", "ΚΩΚΑΚΙΑ ΠΑΣΤΑ"],
    "Λαδόψωμο": ["ΛΑΔΟΨΩΜΟ BREAD", "OIL BREAD", "LADO ΨΩΜΙ"],
    "Λουκανικοπιτάκια": ["ΛΟΥΚΑΝΙΚΟ ΠΙΤΑΚΙΑ", "SAUSAGE PIES", "ΛΟΥΚΑΝΙΚΑ ΠΙΤΑΚΙΑ"],
    "Λουκουμαδάκι": ["ΛΟΥΚΟΥΜΑΔΑΚΙ", "LOUKOUMADAKI", "MINI LOUKOU"],
    "Λουκουμάς": ["ΛΟΥΚΟΥΜΑΣ", "LOUKOUMAS", "GREEK DONUT"],
    "Μαργαρίτα": ["ΜΑΡΓΑΡΙΤΑ", "MARGARITA PIZZA", "PIZZA ΜΑΡΓΑΡΙΤΑ"],
    "Μαύρο Πετρίτης Ερυθρός": ["ΜΑΥΡΟ ΠΕΤΡΙΤΗΣ", "BLACK PETRITIS", "RED WINE PETRITIS"],
    "Μεβγάλ Ελαφρύ": ["ΜΕΒΓΑΛ ΕΛΑΦΡΥ", "MEVGAL LIGHT", "MEVGAL MILK"],
    "Μεβγάλ Πλήρες": ["ΜΕΒΓΑΛ ΠΛΗΡΕΣ", "MEVGAL FULL", "FULL MILK MEVGAL"],
    "Μελομακάρονα Μπουκίτσες και Κουραμπιέδες": ["ΜΕΛΟΜΑΚΑΡΟΝΑ", "KOURAMPIEDES", "MELLOMAKARONA BITE"],
    "Μηλόπιτα Μεγάλη": ["ΜΗΛΟΠΙΤΑ ΜΕΓΑΛΗ", "BIG APPLE PIE", "LARGE MILOPITA"],
    "Μηλόπιτα Μεσαία": ["ΜΗΛΟΠΙΤΑ ΜΕΣΑΙΑ", "MEDIUM APPLE PIE", "MILOPITA ΜΕΣΑΙΟ"],
    "Μηλόπιτα Μικρή": ["ΜΗΛΟΠΙΤΑ ΜΙΚΡΗ", "SMALL APPLE PIE", "MILOPITA ΜΙΚΡΗ"],
    "Μουσταλευριά": ["ΜΟΥΣΤΑΛΕΥΡΙΑ", "MOUSTO LEVRIA", "GRAPE PUDDING"],
    "Μουστοκούλουρα Τραγανά Μαλακά": ["ΜΟΥΣΤΟΚΟΥΛΟΥΡΑ", "MOUS TOKOULOURA", "CRISPY MOUS TOKOULOURA"],
    "Μπαγκέτα Χωριάτικη": ["ΜΠΑΓΚΕΤΑ ΧΩΡΙΑΤΙΚΗ", "VILLAGE BAGUETTE", "ΧΩΡΙΑΤΙΚΗ ΜΠΑΓΚΕΤΑ"],
    "Μπακλαβάς Κομμάτι": ["ΜΠΑΚΛΑΒΑΣ ΚΟΜΜΑΤΙ", "BAKLAVA PIECE", "BAKLAVA KOMMATI"],
    "Μπισκότο Κορμός": ["ΜΠΙΣΚΟΤΟ ΚΟΡΜΟΣ", "BISCUIT LOG", "MΠΙΣΚΟΤΟ ΚΟΡΜΟΣ"],
    "Μπουγάτσα Γλυκιά": ["ΜΠΟΥΓΑΤΣΑ ΓΛΥΚΙΑ", "SWEET BOUGATSA", "ΓΛΥΚΙΑ ΜΠΟΥΓΑΤΣΑ"],
    "Μπριός": ["ΜΠΡΙΟΣ", "BRIOCHE", "BRIOS"],
    "Νεγράκια": ["ΝΕΓΡΑΚΙΑ", "NEGRAKIA", "CHOCOLATE ΝΕΓΡΑΚΙΑ"],
    "Νερό Μικρό": ["ΝΕΡΟ ΜΙΚΡΟ", "SMALL WATER", "MINI WATER"],
    "Πάστες Τεμάχιο": ["ΠΑΣΤΕΣ ΤΕΜΑΧΙΟ", "PASTES PIECE", "PASTES TEM"],
    "Πεϊνιρλάκια": ["ΠΕΙΝΙΡΛΑΚΙΑ", "MINI PEINIRLI", "PEINIRLAKIA"],
    "Πεϊνιρλί Ζαμπόν Τυρί": ["ΠΕΙΝΙΡΛΙ ΖΑΜΠΟΝ", "HAM & CHEESE PEINIRLI", "ΖΑΜΠΟΝ ΠΕΙΝΙΡΛΙ"],
    "Πεϊνιρλί με Λουκάνικο": ["ΠΕΙΝΙΡΛΙ ΛΟΥΚΑΝΙΚΟ", "SAUSAGE PEINIRLI", "ΛΟΥΚΑΝΙΚΟ ΠΕΙΝΙΡΛΙ"],
    "Πιροσκάκια": ["ΠΙΡΟΣΚΑΚΙΑ", "MINI PIROSKI", "PIROSKAKIA"],
    "Πίτσα": ["ΠΙΤΣΑ", "PIZZA", "GREEK PIZZA"],
    "Πολύσπορο": ["ΠΟΛΥΣΠΟΡΟ", "MULTIGRAIN", "MULTI SEED BREAD"],
    "Πολυτέλειας": ["ΠΟΛΥΤΕΛΕΙΑΣ", "LUXURY BREAD", "LUXURY LOAF"],
    "Πορτοκαλόπιτα": ["ΠΟΡΤΟΚΑΛΟΠΙΤΑ", "ORANGE PIE", "PORTOKALOPITA"],
    "Πορτοκαλόπιτα Ταψάκι Μικρό": ["ΠΟΡΤΟΚΑΛΟΠΙΤΑ ΜΙΚΡΟ", "SMALL ORANGE PIE", "PORTOKALO ΜΙΚΡΟ"],
    "Προζύμι Μισό Κιλό": ["ΠΡΟΖΥΜΙ ΜΙΣΟ", "HALF KILO PROZYMI", "ΜΙΣΟ ΚΙΛΟ ΠΡΟΖΥΜΙ"],
    "Πρόσφορο Μικρό": ["ΠΡΟΣΦΟΡΟ ΜΙΚΡΟ", "SMALL PROSFORO", "MINI PROSFORO"],
    "Προφιτερόλ Μεσαίο": ["ΠΡΟΦΙΤΕΡΟΛ ΜΕΣΑΙΟ", "MEDIUM PROFITEROLE", "PROFITEROL ΜΕΣΑΙΟ"],
    "Προφιτερόλ Μεγάλο": ["ΠΡΟΦΙΤΕΡΟΛ ΜΕΓΑΛΟ", "LARGE PROFITEROLE", "PROFITEROL MEΓΑΛΟ"],
    "Σοκολάτα": ["ΣΟΚΟΛΑΤΑ", "CHOCOLATE", "CHOCOLATE DRINK"],
    "Σοκολατόπιτα Κομμάτι": ["ΣΟΚΟΛΑΤΟΠΙΤΑ ΚΟΜΜΑΤΙ", "CHOCOLATE PIECE", "CHOCOLATE PIE KOMMATI"],
    "Σπανακόπιτα Ταψιού": ["ΣΠΑΝΑΚΟΠΙΤΑ", "SPINACH PIE", "SPINACH ΠΙΤΑ"],
    "Σπανακόπιτα Τριγωνή": ["ΣΠΑΝΑΚΟΠΙΤΑ ΤΡΙΓΩΝΗ", "TRIANGLE SPINACH PIE", "ΤΡΙΓΩΝΗ ΣΠΑΝΑΚΟΠΙΤΑ"],
    "Ταρτάκια Διάφορα Λεμονόπιτακια": ["ΤΑΡΤΑΚΙΑ", "LEMON PIECES", "ΤΑΡΤΑΚΙΑ ΛΕΜΟΝΙ"],
    "Τοστ Μαύρο": ["ΤΟΣΤ ΜΑΥΡΟ", "BLACK TOAST", "ΤΟΣΤ ΜΕ ΜΑΥΡΟ ΨΩΜΙ"],
    "Τσάι": ["ΤΣΑΙ", "TEA", "HERBAL TEA"],
    "Τσουρεκάκι Σιροπιαστό Μεγάλο": ["ΤΣΟΥΡΕΚΑΚΙ ΣΙΡΟΠΙΑΣΤΟ", "SYRUPY TSUREKAKI", "SWEET TSUREKAKI"],
    "Τυλιχτά Διάφορα": ["ΤΥΛΙΧΤΑ ΔΙΑΦΟΡΑ", "WRAPPED VARIETY", "VARIETY WRAPS"],
    "Τυρόπιτα Σφολιάτας": ["ΤΥΡΟΠΙΤΑ ΣΦΟΛΙΑΤΑΣ", "PUFF PASTRY PIE", "ΤΥΡΟΠΙΤΑ ΠΙΤΑ"],
    "Τυρόπιτα Ταψιού": ["ΤΥΡΟΠΙΤΑ ΤΑΨΙΟΥ", "PAN CHEESE PIE", "ΤΑΨΙ ΤΥΡΟΠΙΤΑ"],
    "Τυροπιτάκια": ["ΤΥΡΟΠΙΤΑΚΙΑ", "CHEESE PIES", "MINI TYROPITA"],
    "Φάγε Τριμμένο Τυρί Gouda": ["ΦΑΓΕ GOUDA", "GRATED GOUDA", "GOUDA ΦΑΓΕ"],
    "Φαγητά": ["ΦΑΓΗΤΑ", "FOODS", "MEALS"],
    "Φραπέ": ["ΦΡΑΠΕ", "FRAPPE", "FRAPPÉ"],
    "Φραντζολάκια Στρογγυλά": ["ΦΡΑΝΤΖΟΛΑΚΙΑ", "ROUND LOAVES", "ΦΡΑΝΤΖΟΛΑΚΙΑ ΣΤΡΟΓΓ"],
    "Χριστοκούλουρες": ["ΧΡΙΣΤΟΚΟΥΛΟΥΡΕΣ", "CHRISTMAS COOKIES", "ΧΡΙΣΤ ΚΟΥΛΟΥΡΕΣ"],
    "Χωριάτικο Μικρό": ["ΧΩΡΙΑΤΙΚΟ ΜΙΚΡΟ", "SMALL VILLAGE BREAD", "ΜΙΚΡΟ ΧΩΡΙΑΤΙΚΟ"],
    "Ψωμί Προζύμι Ολικής Λευκό": ["ΠΡΟΖΥΜΙ ΟΛΙΚΗΣ", "WHOLE WHEAT BREAD", "WHOLE GRAIN PROZYMI"],
    "Ψωμί της Γιαγιάς": ["ΨΩΜΙ ΓΙΑΓΙΑΣ", "GRANDMA'S BREAD", "ΓΙΑΓΙΑ ΨΩΜΙ"]
}

# Prepare the custom data for training
expanded_data = {"raw_name": [], "standardized_name": []}
for std_name, raw_variants in custom_data.items():
    for variant in raw_variants:
        expanded_data["raw_name"].append(variant)
        expanded_data["standardized_name"].append(std_name)

# Convert the expanded data into a DataFrame
custom_df = pd.DataFrame(expanded_data)

# Combine the original and custom data
combined_df = pd.concat([df, custom_df], ignore_index=True)

# Format the data for training
combined_df['text'] = combined_df.apply(lambda row: f"incorrect_name: {row['raw_name']} -> correct_name: {row['standardized_name']}", axis=1)



# Fine tune the model GPT-2 Small

from transformers import GPT2Tokenizer, GPT2LMHeadModel, Trainer, TrainingArguments
from datasets import Dataset



# Convert the DataFrame to a Dataset object
dataset = Dataset.from_pandas(combined_df[['text']])


















