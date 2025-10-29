from customer import Customer
from order import Order

def main():
    # Create a customer
    customer = Customer(customer_id="C001", name="John Doe", address="123 Elm St")
    
    # Create some orders
    order1 = Order(
        order_id="O1001",
        customer_id="C001",
        item_sku="SKU123",
        item_description="Widget A",
        quantity=2,
        unit_price=19.99
    )
    
    order2 = Order(
        order_id="O1002",
        customer_id="C001",
        item_sku="SKU456",
        item_description="Widget B",
        quantity=1,
        unit_price=29.99
    )
    
    # Add orders to the customer
    customer.add_order(order1)
    customer.add_order(order2)
    
    # Display customer information
    print(customer)
    
    # List all orders for the customer
    for order in customer.list_all_orders():
        print(order)
    
    # Display total number of orders
    print(f"Total Orders: {customer.get_order_count()}")


if __name__ == "__main__":
    main()