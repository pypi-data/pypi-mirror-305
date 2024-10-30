from django.core.management.base import BaseCommand, CommandError
from artd_siigo.utils.siigo_api_util import SiigoApiUtil
from artd_siigo.utils.siigo_db_util import SiigoDbUtil
from artd_partner.models import Partner


class Command(BaseCommand):
    help = "Imports customers from Siigo for a specified partner"

    def add_arguments(self, parser):
        # Define 'partner_slug' argument as required
        parser.add_argument(
            "partner_slug",
            type=str,
            help="The slug for the partner whose customers lists need to be imported",
        )

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS("Importing customers from Siigo..."))
        partner_slug = options["partner_slug"]

        # Validate partner existence
        try:
            partner = Partner.objects.get(partner_slug=partner_slug)
        except Partner.DoesNotExist:
            raise CommandError(f"Partner with slug '{partner_slug}' does not exist")

        try:
            siigo_api = SiigoApiUtil(partner)
            siigo_db = SiigoDbUtil(partner)
            customer = siigo_api.get_all_customers()
            for customer in customer:
                customer_identification = customer["identification"]
                customer_data = {
                    "siigo_id": customer["id"],
                    "siigo_customer_type": siigo_db.get_customer_type(customer["type"]),
                    "siigo_customer_person_type": siigo_db.get_customer_person_type(
                        customer["person_type"]
                    ),
                    "siigo_customer_document_type": siigo_db.get_customer_document_type(
                        customer["id_type"]["code"]
                    ),
                    "identification": customer["identification"],
                    "check_digit": customer["check_digit"],
                    "name": customer["name"],
                    "commercial_name": customer["commercial_name"],
                    "branch_office": customer["branch_office"],
                    "active": customer["active"],
                    "vat_responsible": customer["vat_responsible"],
                    "fiscal_responsibilities": customer["fiscal_responsibilities"],
                    "address": customer["address"],
                    "phones": customer["phones"],
                    "contacts": customer["contacts"],
                    "comments": customer["comments"],
                    "related_users": customer["related_users"],
                    "metadata": customer["metadata"],
                }

                product_obj, created = siigo_db.create_or_update_customer(customer_data)
                if created:
                    self.stdout.write(
                        self.style.SUCCESS(
                            f"Customer '{customer_identification}' created successfully"
                        )
                    )
                else:
                    self.stdout.write(
                        self.style.SUCCESS(
                            f"Customer '{customer_identification}' updated successfully"
                        )
                    )
                self.stdout.write(
                    self.style.NOTICE(
                        f"Customer '{customer_identification}' processed successfully"
                    )
                )
            self.stdout.write(self.style.NOTICE("Customer imported successfully"))

        except Exception as e:
            raise CommandError(f"Error importing customer: {e}")
