class Customer:
    """Represents a Customer with list of Orders.
    Args:
        orders (list): The optional initial list of Orders.
    """

    __total_customers = 0 # protected attribute to track total count of customers

    def __init__(self, name: str, orders: list = []):
        self.name = name
        self.orders = orders
        Customer.__total_customers += 1

    def __repr__(self):
        return f"Customer(name=\"{self.name}\", orders={self.orders})"

    # def __str__(self): will use the __repr__

    @classmethod
    def total_customers(cls):
        """Returns the total number of Customer instances created."""
        return cls.__total_customers

    def add_order(self, order):
        """Adds an Order to the Customer's list of Orders."""
        self.orders.append(order)

    @property
    def total_orders(self):
        """Returns the total number of Orders of the Customer."""
        return len(self.orders)

    @property
    def total_orders_sum(self):
        """Returns the total price-sum of all orders of the Customer."""
        return sum(order.order_sum for order in self.orders)
