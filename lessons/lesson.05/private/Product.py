class BaseProduct:
    type = None

    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f'{self.name} (type = {self.type}, price = {self.price})'

    def __repr__(self):
        return f"{self.__class__.__name__} ('{self.name}', {self.price})"

    def __add__(self, other):
        # return self.__class__(self.price + other.price)
        return BaseProduct('BaseProduct', self.price + other.price)

    def make_discount(self, discount):
        self.price *= (100 - discount) / 100


class Laptop(BaseProduct):
    type = 'Laptop'


class MobilePhone(BaseProduct):
    def __init__(self, name, price):
        super().__init__(name, price)

    type = 'Mobile Phone'


class Basket:

    # искажение имени аттрибута _Basket__items
    def __init__(self):
        self.__items = []
        self._discount = 0

    @property
    def items(self):
        return self.__items

    @items.setter
    def items(self, val):
        self.__iadd__(val)

    def __iadd__(self, product):
        self.__items.append(product)
        return self

    def add(self, product):
        self.__items.append(product)

    def __len__(self):
        return len(self.__items)

    def __iter__(self):
        return (el for el in self.__items)


samsung_note_10 = MobilePhone('Samsung Galaxy Note 10', 1000)
mac_pro = Laptop('Macbook Pro 16"', 3500)
nokia = MobilePhone("Nokia 3310", 50)

basket = Basket()
print(basket._discount)
print(basket.__items)

# print(vars(getattribute))
# print(getattribute.__items)
print(basket._discount)
