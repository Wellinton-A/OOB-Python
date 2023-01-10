class Item:
    rate_disc = 0.8

    all = []
    def __init__(self, name: str, price: float, quantity: int):
        self.name = name
        self.price = price
        self.quantity = quantity

        Item.all.append(self)
    
    def __repr__(self):
        return f"Item('{self.name}', {self.price}, {self.quantity})"

    def sold_item(self, n: int):
        self.quantity = self.quantity - n
    
    def add_item(self, n: int):
        self.quantity = self.quantity + n

    def total_value_items(self):
        return self.quantity * self.price

item1 =Item('Laptop', 999.90, 50)
item2 =Item('Keyboard', 47.80, 150)
item3 =Item('Mouse', 25.99, 100)
item4 =Item('TV', 749.50, 25)
item5 =Item('PS5', 1499.90, 10)
item6 =Item('Monitor', 999.90, 30)
item7 =Item('Ball', 5.9, 500)
item8 =Item('Smartphone', 1050.99, 50)
item9 =Item('CPU', 1350.79, 10)
item10 =Item('RAM Memory', 250, 850)
item11 =Item('Smartwatch', 500.80, 450)
item12 =Item('Dog', 1875.89, 550)

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
    
