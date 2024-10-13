placed_order = [
    ("Alice", "Laptop", 1),
    ("Bob", "Camera", 2),
    ("Misty", "Cell phone", 1),
    ("Sarah", "Game controller", 4)
]
def unpack_me(customer_order_info):
    for order in customer_order_info:
        customer_name, product, quantity = order
        format_details = f'Customer: {customer_name} \nProduct: {product} \nQuantity: {quantity}'
        print("\n" + format_details)

unpack_me(placed_order)