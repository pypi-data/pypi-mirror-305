from django.core.management.base import BaseCommand, CommandError
from artd_siigo.utils.siigo_api_util import SiigoApiUtil
from artd_siigo.utils.siigo_db_util import SiigoDbUtil
from artd_partner.models import Partner


class Command(BaseCommand):
    help = "Imports products from Siigo for a specified partner"

    def add_arguments(self, parser):
        # Define 'partner_slug' argument as required
        parser.add_argument(
            "partner_slug",
            type=str,
            help="The slug for the partner whose products lists need to be imported",
        )

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS("Importing producs from Siigo..."))
        partner_slug = options["partner_slug"]

        # Validate partner existence
        try:
            partner = Partner.objects.get(partner_slug=partner_slug)
        except Partner.DoesNotExist:
            raise CommandError(f"Partner with slug '{partner_slug}' does not exist")

        try:
            siigo_api = SiigoApiUtil(partner)
            siigo_db = SiigoDbUtil(partner)
            products = siigo_api.get_all_products()
            for product in products:
                siigo_id = product["id"]
                code = product["code"]
                name = product["name"]
                account_group = product["account_group"]
                account_group_id = account_group["id"]
                siigo_account_group = siigo_db.get_account_group(account_group_id)
                type = product["type"]
                stock_control = product["stock_control"]
                active = product["active"]
                tax_classification = product["tax_classification"]
                tax_included = product["tax_included"]
                tax_consumption_value = product["tax_consumption_value"]
                taxes = product["taxes"]
                siigo_taxes = []
                for tax in taxes:
                    tax_id = tax["id"]
                    siigo_tax = siigo_db.get_siigo_tax(tax_id)
                    siigo_taxes.append(siigo_tax)
                unit_label = product["unit_label"]
                unit = product["unit"]
                unit_obj, created = siigo_db.update_or_create_unit(unit)
                if created:
                    self.stdout.write(
                        self.style.SUCCESS(
                            f"Unit '{unit_label}' created successfully---"
                        )
                    )
                else:
                    self.stdout.write(
                        self.style.SUCCESS(
                            f"Unit '{unit_label}' updated successfully---"
                        )
                    )
                reference = product["reference"]
                description = product["description"]
                additional_fields = product["additional_fields"]
                available_quantity = product["available_quantity"]
                metadata = product["metadata"]
                product_data_dict = {
                    "siigo_id": siigo_id,
                    "code": code,
                    "name": name,
                    "account_group": siigo_account_group,
                    "type": type,
                    "stock_control": stock_control,
                    "active": active,
                    "tax_classification": tax_classification,
                    "tax_included": tax_included,
                    "tax_consumption_value": tax_consumption_value,
                    "unit_label": unit_label,
                    "unit": unit_obj,
                    "reference": reference,
                    "description": description,
                    "additional_fields": additional_fields,
                    "available_quantity": available_quantity,
                    "metadata": metadata,
                    "json_data": product,
                }
                product_obj, created = siigo_db.create_or_update_product(
                    product_data_dict
                )
                if created:
                    self.stdout.write(
                        self.style.SUCCESS(f"Product '{name}' created successfully")
                    )
                else:
                    self.stdout.write(
                        self.style.SUCCESS(f"Product '{name}' updated successfully")
                    )
                warehouses = product["warehouses"]
                siigo_warehouses = []
                for warehouse in warehouses:
                    siigo_warehouse = siigo_db.get_warehouse(warehouse["id"])
                    siigo_warehouses.append(siigo_warehouse)
                if len(siigo_warehouses) > 0:
                    product_obj.warehouses.set(siigo_warehouses)
                siigo_taxes = []
                for tax in taxes:
                    siigo_tax = siigo_db.get_siigo_tax(tax["id"])
                    siigo_taxes.append(siigo_tax)
                    pass
                if len(siigo_taxes) > 0:
                    product_obj.taxes.set(siigo_taxes)
                prices = product["prices"]
                siigo_db.get_or_update_prices(product_obj, prices)
                self.stdout.write(
                    self.style.NOTICE(f"Product '{name}' processed successfully")
                )
            self.stdout.write(self.style.NOTICE("Products imported successfully"))

        except Exception as e:
            raise CommandError(f"Error importing products: {e}")
