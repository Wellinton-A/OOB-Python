import csv


class Item:
    rate_disc = 0.8

    all = []

    def __init__(self, name: str, price: float, quantity: int):
        self.name = name
        self.price = price
        self.__quantity = quantity

        Item.all.append(self)

    @property
    def quantity(self):
        return self.__quantity

    @classmethod
    def sold_item(self, name_of: str, n: int):
        for i in Item.all:
            if i.name == name_of:
                i.__quantity = i.__quantity - n

    @classmethod
    def add_item(self, name_of: str, n: int):
        for i in Item.all:
            if i.name == name_of:
                i.__quantity = i.__quantity + n

    def total_value_items(self):
        return self.__quantity * self.price

    @classmethod
    def dict_price_items(cls):
        for i in Item.all:
            dict_items.update({i.name: i.price})

    @classmethod
    def max_value_item(cls):
        key_list = list(dict_items.keys())
        value_list = list(dict_items.values())
        max_value = {key_list[value_list.index(
            max(value_list))]: max(value_list)}
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
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.__quantity})"


class Phones(Item):
    all = []

    def __init__(self, name: str, price: float, quantity=0, broken=0):
        super().__init__(name, price, quantity)
        self.broken = broken

        Phones.all.append(self)
    
    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity}, {self.broken})"

    @classmethod
    def fix_broken_phones(cls, name, n):
        for i in Phones.all:
            if i.name == name:
                i.broken += n


Item.instantiate_from_csv()
dict_items = {}
Phones('Phone1', 99.90, 10, 5)
print(Item.obj_type(dict_items))
Item.dict_price_items()
Item.max_value_item()
Item.add_item('Laptop', 5)
# Item.sold_item(name_of=(input("Nome do item: ")), n=(input("Quantidade: ")))
Phones.fix_broken_phones('Phone1', 2)
print(Phones.all)
print(Item.all)
# print(dir(int()))
