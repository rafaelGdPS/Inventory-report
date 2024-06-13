from typing import Optional

from inventory_report.product import Product


class Inventory:
    def __init__(self, data: Optional[list[Product]] = None) -> None:
        self.__data = [] if not data else data

    @property
    def data(self):
        return self.__data

    def add_data(self, data: list[Product]):
        self.data.extend(data)
