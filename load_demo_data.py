"""
Script pour charger des données de démonstration.
Usage: python manage.py shell < load_demo_data.py
"""
import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ecommerce.settings')
django.setup()

from shop.models import Category, Product

# Catégories
cat1, _ = Category.objects.get_or_create(name="Électronique", slug="electronique")
cat2, _ = Category.objects.get_or_create(name="Vêtements", slug="vetements")
cat3, _ = Category.objects.get_or_create(name="Livres", slug="livres")

# Produits
products_data = [
    {"name": "Smartphone Pro X", "slug": "smartphone-pro-x", "category": cat1, "price": 699.99, "stock": 15, "description": "Smartphone dernière génération avec écran AMOLED 6.7 pouces."},
    {"name": "Casque Bluetooth", "slug": "casque-bluetooth", "category": cat1, "price": 89.99, "stock": 30, "description": "Casque sans fil avec réduction de bruit active. Autonomie 30h."},
    {"name": "Tablette Ultra", "slug": "tablette-ultra", "category": cat1, "price": 349.00, "stock": 8, "description": "Tablette 10 pouces, idéale pour le travail et les loisirs."},
    {"name": "T-shirt Premium", "slug": "tshirt-premium", "category": cat2, "price": 29.99, "stock": 50, "description": "T-shirt 100% coton biologique, coupe moderne."},
    {"name": "Veste en jean", "slug": "veste-jean", "category": cat2, "price": 79.99, "stock": 20, "description": "Veste en denim classique, disponible en plusieurs tailles."},
    {"name": "Python pour tous", "slug": "python-pour-tous", "category": cat3, "price": 24.90, "stock": 100, "description": "Apprenez Python de zéro à avancé avec des exercices pratiques."},
    {"name": "Django en pratique", "slug": "django-en-pratique", "category": cat3, "price": 34.90, "stock": 75, "description": "Créez des applications web professionnelles avec Django."},
]

for data in products_data:
    Product.objects.get_or_create(slug=data['slug'], defaults=data)

print(f"✅ {Category.objects.count()} catégories et {Product.objects.count()} produits créés !")
