"""
    Restaurant Revisted Exersice

- Add setters and getters to all subclasses for menu item.

- Override calculate_total_price() according to the order 
composition (e.g if the order includes a main course apply some 
disccount on beverages). 

- Add the class Payment() following the class example.
"""

class MenuItem:
    """
    Clase base que representa un artículo del menú en el restaurante.
    Tiene atributos para el nombre, precio y descuento.
    """
    def __init__(self, name: str, price: float, discount: float = 0.0):
        # Validación de tipos de datos de cada uno de los argumentos.
        if not isinstance(name, str):
            raise TypeError("El nombre debe ser un string.")
        if not isinstance(price, (int, float)) or price < 0:
            raise ValueError("El precio debe ser un número positivo.")
        if not (0 <= discount <= 1):
            raise ValueError("El descuento debe ser entre 0 a 1 (0% a 100%).")

        self.__name = name
        self.__price = price
        self.__discount = discount

    # Getters y setters.
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        self.__price = value

    @property
    def discount(self):
        return self.__discount

    @discount.setter
    def discount(self, value):
        self.__discount = value

    def calculate(self) -> float:
        return self.__price * (1 - self.__discount)

    def __str__(self):
        discount_price = self.calculate()
        if self.__discount > 0:
            return (f"{self.__name}: ${self.__price:.2f} "
                    f"(Descuento: ${discount_price:.2f})")
        return f"{self.__name}: ${self.__price:.2f}"

# Clases que heredan de MenuItem.
# Subclases con getters y setters.
class Beverage(MenuItem):
    pass

class Appetizers(MenuItem):
    pass

class SideDishes(MenuItem):
    pass

class MainCourses(MenuItem):
    pass

class Desserts(MenuItem):
    pass

class Order:
    def __init__(self):
        self.items = []

    def add_item(self, item: MenuItem):
        self.items.append(item)

    def bill_amount(self) -> float:
        return sum(item.calculate() for item in self.items)

    def calculate_total_price(self) -> float:
        total = self.bill_amount()
        has_main_course = any(isinstance(item, MainCourses) for item in self.items)
        if has_main_course:
            total -= sum(item.calculate() * 0.1 for item in self.items if isinstance(item, Beverage))
        return total

class Payment:
    def __init__(self, order: Order, payment_method: str):
        if payment_method not in ("efectivo", "tarjeta"):
            raise ValueError(
                "Método de pago inválido. Elige entre"
                "'efectivo' o 'tarjeta'.")
        self.order = order
        self.payment_method = payment_method

    def process_payment(self):
        total = self.order.calculate_total_price()
        return f"Pago de ${total:.2f} procesando con {self.payment_method}."

# Lista de productos 
menu = [
    Beverage("Coca Cola", 2.5),
    Beverage("Sprite", 1.5),
    Beverage("Water", 1.0),
    Appetizers("Fries", 3.0),
    Appetizers("Egg Rolls", 3.0),
    Appetizers("Crab Chips", 3.0),
    SideDishes("Tacos", 4.0),
    SideDishes("Soup", 3.0),
    SideDishes("Salad", 2.0),
    SideDishes("Charred Sweetcorn Salsa", 6.0),
    MainCourses("Burger", 5.0),
    MainCourses("Chicken Fried Steak", 6.0),
    MainCourses("Pizza", 8.0),
    Desserts("Cake", 3.5),
    Desserts("Ice Cream", 4.0)
]

# Creación de una orden
beverage = Beverage("Coca Cola", 2.5, 0.2)   
appetizer = Appetizers("Fries", 3.0, 0.05)
side_dish = SideDishes("Tacos", 4.0, 0.05)
main_course = MainCourses("Burger", 5.0, 0.1)
dessert = Desserts("Cake", 3.5)

order = Order()
order.add_item(beverage)
order.add_item(appetizer)
order.add_item(side_dish)
order.add_item(main_course)
order.add_item(dessert)

print("Esta es tu orden:")
for item in order.items:
    print(item)

print("Precio total:", order.bill_amount())
print("Precio total con descuento:", order.calculate_total_price())

payment = Payment(order, "tarjeta")
print(payment.process_payment())
