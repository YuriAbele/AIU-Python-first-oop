class Product:
    """Represents a product with a name and price.
    Args:
        name (str): The name of the product.
        price (float): The price of the product.
    """
    
    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price
        
    def __repr__(self):
        return f"Product(name=\"{self.name}\", price={self.price})"
    
    # def __str__(self): will use the __repr__
    
    def __eq__(self, value):
        if not isinstance(value, Product):
            return False
        return self.name == value.name and self.price == value.price
    
    def __lt__(self, value):
        if not isinstance(value, Product):
            return NotImplemented
        return self.price < value.price
