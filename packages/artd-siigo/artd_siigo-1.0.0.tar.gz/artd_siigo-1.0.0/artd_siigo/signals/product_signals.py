from artd_partner.models import Partner
from artd_product.models import Product
from django.db.models.signals import post_save
from django.dispatch import receiver
from artd_siigo.utils.siigo_api_util import SiigoApiUtil
from artd_siigo.models import (
    ProductTypeMapping,
    SiigoProductType,
    SiigoProductProxy,
    TaxMapping,
    SiigoTax,
)


@receiver(post_save, sender=Product)
def create_artd_product(
    sender: Product,
    instance: Product,
    created: bool,
    **kwargs,
) -> None:
    product: Product = instance
    partner: Partner = product.partner
    siigo_api_util = SiigoApiUtil(partner=partner)
    try:
        product_type_mapping = ProductTypeMapping.objects.get(
            product_type=product.type,
            partner=partner,
        )
        siigo_product_type: SiigoProductType = product_type_mapping.siigo_product_type
        siigo_product_proxy: SiigoProductProxy = product.siigoproductproxy
        siigo_account_group = siigo_product_proxy.siigo_account_group
        tax = product.tax
        tax_mapping = TaxMapping.objects.get(
            tax=tax,
            partner=partner,
        )
        siigo_tax: SiigoTax = tax_mapping.siigo_tax
        taxes = []
        tax_dict = {
            "id": siigo_tax.siigo_id,
            "name": siigo_tax.name,
            "type": siigo_tax.type,
            "percentage": siigo_tax.percentage,
        }
        taxes.append(tax_dict)
        product_data = {
            "code": product.sku,
            "name": product.name,
            "account_group": siigo_account_group.siigo_id,
            "type": siigo_product_type.code,
            "active": product.status,
            "taxes": taxes,
        }
        response = siigo_api_util.create_product(product_data)
        if "status_code" not in response:
            print(f"Response: {response}")
    except Exception as e:
        print(e)
