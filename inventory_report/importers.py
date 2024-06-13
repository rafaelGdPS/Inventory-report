import json
from abc import ABC, abstractmethod
from typing import Dict, Type

from inventory_report.product import Product


class Importer(ABC):
    def __init__(self, path: str) -> None:
        self.path_file = path

    @abstractmethod
    def import_data(self) -> list[Product]:
        ...


class JsonImporter(Importer):
    def __init__(self, path: str) -> None:
        super().__init__(path)

    def import_data(self) -> list[Product]:
        product_list = []

        with open(self.path_file) as file:
            products = json.load(file)

        for product in products:
            new_product = Product(
               product["id"],
               product["product_name"],
               product["company_name"],
               product["manufacturing_date"],
               product["expiration_date"],
               product["serial_number"],
               product["storage_instructions"],
            )
            product_list.append(new_product)
        
        return product_list


class CsvImporter:
    pass


# Não altere a variável abaixo

IMPORTERS: Dict[str, Type[Importer]] = {
    "json": JsonImporter,
    "csv": CsvImporter,
}
