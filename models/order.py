class Order:
    """Represents a Order with list of Products.
    Args:
        products (list): The optionsl initial list of Product.
    """

    __total_orders = 0 # protected attribute to track total count of orders
    __total_orders_sum = 0.0 # protected attribute to track total count of orders

    def __init__(self, products: list = []):
        self.products = products
        Order.__total_orders += 1 # increment total orders count
        Order.__total_orders_sum += sum(product.price for product in products) # increment total order prices with sum of prices of all products in the order

    def __repr__(self):
        return f"Order(products={self.products})"

    # def __str__(self): will use the __repr__

    @classmethod
    def total_orders(cls):
        """Returns the total number of Order instances created."""
        return cls.__total_orders

    @classmethod
    def total_orders_sum(cls):
        """Returns the total price-sum of all orders."""
        return cls.__total_orders_sum

    def add_product(self, product):
        """Adds a Product to the Order's list of Products."""
        self.products.append(product)
        Order.__total_orders_sum += product.price # increment total order prices with price of added product

    @property
    def order_sum(self):
        """Returns the total price-sum of the order."""
        return sum(product.price for product in self.products)
    