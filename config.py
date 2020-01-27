
# DATABASE configuration

HOST = "localhost"
USER = "openff"
PWD = "openff"

TABLE_PRODUCT = "product"
TABLE_CATEGORY = "category"
TABLE_STORE = "store"
DB = "open_ff"

# MENU configuration

WELCOME = [
    "Mettre à jour les produits",
    "Rechercher un produit",
    "Consulter les produits sauvegardés",
    "Quit",
]

CATEGORIES = [
    "Confitures de fruits rouges",
    "Pâtes à tartiner aux noisettes",
    "Brioches",
    "Jus de fruits",
]

HISTORY = [
    "Sauvegarder produit(s)",
    "Consulter produit(s)",
    "Supprimer produit(s)",
    "Rechercher un produit",
    "Quit",
]

# API configuration, items and filters

PAGE_SIZE = 200

FILTER = (
    "nutrition_grade_fr",
    "quantity",
    "url",
    "brands",
    "categories",
    "code",
    "product_name",
    "stores",
)
