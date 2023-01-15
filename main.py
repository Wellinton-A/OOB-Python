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
    def dict_price_items(cls):
        for i in Item.all:
            dict_items.update({i.name: i.price})

    @classmethod
    def max_value_item(cls):
        key_list = list(dict_items.keys())
        value_list = list(dict_items.values())
        max_value = {key_list[value_list.index(max(value_list))]: max(value_list)}
        print(f'the most valuable stock of items is: {max_value}')

    @classmethod
    def instantiate_from_csv(cls):
        with open('items.csv', 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)

        for item in items:
            Item(
                name=item.get('name'),
                price=float(item.get('price')),
                quantity=int(item.get('quantity')),
            )
    
    @staticmethod
    def obj_type(obj):
        if isinstance(obj, type(obj)):
            return f'\'{obj}\' is a {type(obj)}'
        else:
            return False



    def __repr__(self):
        return f"Item('{self.name}', {self.price}, {self.quantity})"


Item.instantiate_from_csv()
dict_items = {}
# print(Item.all)
print(Item.obj_type(dict_items))
Item.dict_price_items()
Item.max_value_item()







