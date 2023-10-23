
class Product:

    def __init__(self, name: str, brand, model, price) -> None:
        self.name = name
        self.brand = brand
        self.model = model
        self.price = price


product1 = Product("tele", "sumsung", "HAA", 999000)

print(product1.name)