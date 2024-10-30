from django.core.management.base import BaseCommand, CommandError
from artd_siigo.models import SiigoDocumentType
from artd_siigo.utils.siigo_api_util import SiigoApiUtil
from artd_partner.models import Partner


class Command(BaseCommand):
    help = "Imports document types from Siigo for a specified partner"

    def add_arguments(self, parser):
        # Define 'partner_slug' argument as required
        parser.add_argument(
            "partner_slug",
            type=str,
            help="The slug for the partner whose document types need to be imported",
        )

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS("Importing document types from Siigo..."))
        partner_slug = options["partner_slug"]
        # Validate partner existence
        try:
            partner = Partner.objects.get(
                partner_slug=partner_slug
            )  # Adjust this line if the slug field is named differently
        except Partner.DoesNotExist:
            raise CommandError(f"Partner with slug '{partner_slug}' does not exist")

        try:
            siigo_api = SiigoApiUtil(partner)
            document_types = (
                siigo_api.get_document_types()
            )  # This method should retrieve the document types from the API

            for doc_type in document_types:
                SiigoDocumentType.objects.update_or_create(
                    siigo_id=doc_type["id"],
                    partner=partner,
                    defaults={
                        "code": doc_type["code"],
                        "name": doc_type["name"],
                        "description": doc_type["description"],
                        "type": doc_type["type"],
                        "active": doc_type["active"],
                        "seller_by_item": doc_type["seller_by_item"],
                        "cost_center": doc_type["cost_center"],
                        "cost_center_mandatory": doc_type["cost_center_mandatory"],
                        "automatic_number": doc_type["automatic_number"],
                        "consecutive": doc_type["consecutive"],
                        "discount_type": doc_type["discount_type"],
                        "decimals": doc_type["decimals"],
                        "advance_payment": doc_type["advance_payment"],
                        "reteiva": doc_type["reteiva"],
                        "reteica": doc_type["reteica"],
                        "self_withholding": doc_type["self_withholding"],
                        "self_withholding_limit": doc_type["self_withholding_limit"],
                        "electronic_type": doc_type["electronic_type"],
                        "cargo_transportation": doc_type["cargo_transportation"],
                        "healthcare_company": doc_type["healthcare_company"],
                        "customer_by_item": doc_type["customer_by_item"],
                        "json_data": doc_type,  # Store the entire document type as JSON
                    },
                )
            self.stdout.write(
                self.style.SUCCESS("Document types imported successfully")
            )

        except Exception as e:
            raise CommandError(f"Error importing document types: {e}")
