from datetime import datetime
from models.customer import Customer
from models.discount import Discount
from models.order import Order
from models.product import Product

# INIT DATA
print("\n--- INIT DATA ---")

product1 = Product(name="First Product", price=11.11)
product2 = Product(name="Second Product", price=22.22)
product3 = Product(name="Third Product", price=33.33)

product4 = Product(name="Fourth Product", price=44.44)
product5 = Product(name="Fifth Product", price=55.55)

product6 = Product(name="Sixth Product", price=66.66)

order1 = Order([product1])
order2 = Order([product2, product3])
order3 = Order([product4, product5, product6])

customer1 = Customer("XYZ-Consulting", [order1])
customer1.add_order(order2)
customer2 = Customer("Horns and hooves")
customer2.add_order(order3)

print(product1, product2, product3, sep="\n", end="\n\n")
print(order1, order2, order3, sep="\n", end="\n\n")
print(customer1, customer2, sep="\n", end="\n")

# CLASS METHODS TESTS
print("\n--- CLASS METHODS TESTS ---")
print(f"Total customers created:\n\t{Customer.total_customers()}")
print(f"Total orders created:\n\t{Order.total_orders()}")
print(f"Total sum of all orders of all customers:\n\t{Order.total_orders_sum():.2f}$")

# DISCOUNT TESTS
print("\n--- DISCOUNT TESTS ---")
TEST_PRICE = 1000.0
special_discount = Discount("Special discount", 22.0)
test_prise_with_special_discount = special_discount.apply(TEST_PRICE)
print(f"TestPrice={TEST_PRICE}$, after applying of Special-Discount={special_discount.discount_percent}% will be reduced to {test_prise_with_special_discount}$.")

test_prise_with_seasonal_discount = Discount.apply_seasonal_discount(TEST_PRICE)
print(f"TestPrice={TEST_PRICE}$, after applying of Seasonal-Discount will be reduced to {test_prise_with_seasonal_discount}$.")

for promo_code in ["Black Friday", "Cyber Monday", "Christmas", "New Year", "Unknown"]:
	test_prise_with_promo_discount = Discount.apply_promo_discount(TEST_PRICE, promo_code)
	print(f"TestPrice={TEST_PRICE}$, after applying of \"{promo_code}\" Promo-Discount will be reduced to {test_prise_with_promo_discount}$.")

# TEST ALL TOGETHER
print("\n--- TEST ALL TOGETHER ---")
test_order_1 = Order([product1, product2])
test_order_2 = Order([product4, product5])
test_customer = Customer("Test-Customer", [test_order_1, test_order_2])
print(test_customer, end="\n\n")
print(f"Total orders of {test_customer.name}:\n\t{test_customer.total_orders}")
print(f"Total sum of all orders of {test_customer.name}:\n\t{test_customer.total_orders_sum:.2f}$")
test_customer_total_with_discount = Discount.apply_promo_discount(test_customer.total_orders_sum, "Black Friday")
print(f"Total sum of all orders of {test_customer.name} with \"Black Friday\" discount:\n\t{test_customer_total_with_discount:.2f}$\n")

print(f"Finished at: {datetime.now():%Y-%m-%d %H:%M:%S}\n\n")
# End of main.py