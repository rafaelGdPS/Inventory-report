from inventory_report.inventory import Inventory
from inventory_report.reports.report import Report
from datetime import date


class SimpleReport(Report):
    def __init__(self) -> None:
        self.inventory: list[Inventory] = []

    def add_inventory(self, inventory: Inventory) -> None:

        self.inventory.append(inventory)

    def generate(self) -> str:
        products_companies: dict[str, int] = {}

        expiration_date = str(date.today())
        all_expiration_date = []

        manufacturing_date = []

        for inventory in self.inventory:
            for product in inventory.data:

                manufacturing_date.append(product.manufacturing_date)

                if product.expiration_date >= expiration_date:
                    all_expiration_date.append(product.expiration_date)

                if product.company_name not in products_companies:
                    products_companies[product.company_name] = 1
                else:
                    products_companies[product.company_name] += 1

        largest_inventory = max(products_companies, key=products_companies.get)
        next_expiration_date = min(all_expiration_date)
        oldest_manufacturing_date = min(manufacturing_date)

        return (
            f"Oldest manufacturing date: {oldest_manufacturing_date}\n"
            f"Closest expiration date: {next_expiration_date}\n"
            f"Company with the largest inventory: {largest_inventory}\n"
        )


