# ShopDjango — Site E-Commerce

## Installation rapide

### 1. Créer un environnement virtuel
```bash
python -m venv venv
source venv/bin/activate      # Linux/Mac
venv\Scripts\activate         # Windows
```

### 2. Installer les dépendances
```bash
pip install -r requirements.txt
```

### 3. Initialiser la base de données
```bash
python manage.py migrate
```

### 4. Créer un compte administrateur
```bash
python manage.py createsuperuser
```

### 5. Lancer le serveur
```bash
python manage.py runserver
```

### 6. Accéder au site
- **Site** → http://127.0.0.1:8000/
- **Admin** → http://127.0.0.1:8000/admin/

---

## Ajouter des produits

1. Aller sur http://127.0.0.1:8000/admin/
2. Se connecter avec votre compte admin
3. Créer des **Catégories** (avec un slug ex: `electronique`)
4. Créer des **Produits** en les liant à une catégorie

---

## Structure du projet

```
ecommerce/
├── ecommerce/          # Configuration Django
│   ├── settings.py
│   └── urls.py
├── shop/               # Catalogue produits
├── cart/               # Panier (session)
├── orders/             # Commandes
├── users/              # Authentification
├── templates/          # Template de base
├── media/              # Images uploadées
├── manage.py
└── requirements.txt
```

## Fonctionnalités

- ✅ Catalogue produits avec catégories
- ✅ Recherche par nom
- ✅ Panier en session (sans compte requis)
- ✅ Passage de commande
- ✅ Historique des commandes
- ✅ Inscription / Connexion utilisateur
- ✅ Interface admin complète
- ✅ Design responsive Bootstrap 5
