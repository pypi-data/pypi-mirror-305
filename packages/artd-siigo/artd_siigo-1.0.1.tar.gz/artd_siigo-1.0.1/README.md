# ArtD SIIGO

The SIIGO package developed by ArtD, allows the integration of the Colombian ERP SIIGO, is responsible for importing the data to then be approved and the subsequent incorporation of data within SIIGO, data such as clients, products and accounting vouchers.

## How to use?

1. Install The package
```bash
pip install artd-siigo
```

2. Add the required on settings.py as follows
```python
INSTALLED_APPS = [
    "dal",
    "dal_select2",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django_extensions",
    "django_json_widget",
    "artd_location",
    "artd_modules",
    "artd_partner",
    "artd_service",
    "artd_urls",
    "artd_product",
    "artd_customer",
    "artd_promotion",
    "artd_order",
    "artd_siigo",
]

```
3. Run the migrations command
```bash
python manage.py migrate
```

4. Run the base commands
```bash
python manage.py create_countries
python manage.py create_colombian_regions
python manage.py create_colombian_cities
python manage.py create_taxes
python manage.py create_apps
python manage.py create_services
python manage.py insert_installed_apps_and_permissions
python manage.py populate_customer_types your_partner_slug
python manage.py populate_customer_person_types your_partner_slug
python manage.py populate_customer_document_types your_partner_slug
python manage.py map_locations
```

5. Create a superuser
```bash
python manage.py createsuperuser
```

6. Log in to your Django instance manager

7. Create a partner

8. Configure your SIIGO credencials

9. Import the data from SIIGO
```bash
python manage.py import_account_groups_from_siigo your_partner_slug
python manage.py import_taxes_from_siigo your_partner_slug
python manage.py import_price_lists_from_siigo your_partner_slug
python manage.py import_warehouses_from_siigo your_partner_slug
python manage.py import_users_from_siigo your_partner_slug
python manage.py import_document_types_from_siigo your_partner_slug
python manage.py import_payment_types_from_siigo your_partner_slug
python manage.py import_cost_center_from_siigo your_partner_slug
python manage.py import_fixed_assets_from_siigo your_partner_slug
python manage.py import_fixed_assets_from_siigo your_partner_slug
python manage.py import_customers_from_siigo your_partner_slug
python manage.py import_product_types_from_siigo your_partner_slug
python manage.py import_products_form_siigo your_partner_slug
```
