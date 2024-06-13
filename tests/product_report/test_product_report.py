from inventory_report.product import Product


def test_product_report() -> None:
    id = "5"
    company_name = "Test&&CIA"
    product_name = "Iogurt"
    manufacturing_date = "2024/06/13"
    expiration_date = "24/07/13"
    serial_number = "555724"
    storage_instructions = "Armazenar sempre em lugares refrigerados"
    product = Product(
        id,
        product_name,
        company_name,
        manufacturing_date,
        expiration_date,
        serial_number,
        storage_instructions,
    )
    assert f"The product {id} - {product_name} " in product.__str__()
    assert f"with serial number {serial_number} " in product.__str__()
    assert f"manufactured on {manufacturing_date} " in product.__str__()
    assert f"by the company {company_name} " in product.__str__()
    assert f"valid until {expiration_date} " in product.__str__()
    assert (
        "must be stored according to the following instructions: "
        f"{storage_instructions}." in product.__str__()
        )
