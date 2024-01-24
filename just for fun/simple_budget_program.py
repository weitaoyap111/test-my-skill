import datetime
from pprint import pprint


class Budget(object):
    transaction_list = []
    def __init__(self):
        pass

    def create_transaction(self, date, amount, category, description=""):
        self.transaction_list.append({
            "date": date,
            "amount": amount,
            "category": category,
            "description": description if description != "" else category,
        })

b = Budget()
b.create_transaction(date=datetime.date(2023, 9, 1), amount=5000, category="Salary")
b.create_transaction(date=datetime.date(2023, 9, 2), amount=-30, category="Food")

pprint(b.transaction_list)
