import csv

class Item:
    rate_disc = 0.8

    all = []

    def __init__(self, name: str, price: float, quantity: int):
        self.name = name
        self.price = price
        self.quantity = quantity

        Item.all.append(self)

    def sold_item(self, n: int):
        self.quantity = self.quantity - n

    def add_item(self, n: int):
        self.quantity = self.quantity + n

    def total_value_items(self):
        return self.quantity * self.price

    @classmethod
    def instantiate_from_csv(cls):
        with open('items.csv','r') as f:
            reader = csv.DictReader(f)
            items = list(reader)
        
        for item in items:
            Item(
                name=item.get('name'),
                price=float(item.get('price')),
                quantity=int(item.get('quantity')),
            )

    def __repr__(self):
        return f"Item('{self.name}', {self.price}, {self.quantity})"


Item.instantiate_from_csv()

print(Item.all)
dict_items = {}


def dict_all_items():
    for i in Item.all:
        dict_items.update({i.name: i.price})


dict_all_items()


def max_value_item():
    key_list = list(dict_items.keys())
    value_list = list(dict_items.values())
    max_value = {key_list[value_list.index(max(value_list))]: max(value_list)}
    return max_value

print(max_value_item())
