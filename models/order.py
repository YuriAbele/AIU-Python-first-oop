class Order:
    """Represents a Order with list of Products.
    Args:
        products (list): The optionsl initial list of Product.
    """
    
    _total_orders = 0 # protected attribute to track total count of orders

    def __init__(self, products: list = []):
        self.products = products
        Order._total_orders += 1
        
    def __repr__(self):
        return f"Order(products={self.products})"
    
    def __str2__(self):
        return f"Order with {len(self.products)} products."
    
    @property
    def total_orders(cls):
        """Returns the total number of Order instances created."""
        return cls._total_orders
