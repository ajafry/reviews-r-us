from typing import List
from order import Order

class Customer:
    def __init__(self, customer_id: str, name: str, address: str):
        """
        Initialize a Customer instance.
        
        Args:
            customer_id (str): Unique identifier for the customer
            name (str): Customer's name
            address (str): Customer's address
        """
        self.customer_id = customer_id
        self.name = name
        self.address = address
        self.orders: List[Order] = []
    
    def add_order(self, order: Order) -> None:
        """
        Add an order to the customer's order list.
        
        Args:
            order (Order): Order instance to add
        """
        self.orders.append(order)
    
    def list_all_orders(self) -> List[Order]:
        """
        Get all orders for this customer.
        
        Returns:
            List[Order]: List of all orders
        """
        return self.orders.copy()
    
    def get_order_count(self) -> int:
        """
        Get the total number of orders for this customer.
        
        Returns:
            int: Number of orders
        """
        return len(self.orders)
    
    def __str__(self) -> str:
        """String representation of the customer."""
        return f"Customer(ID: {self.customer_id}, Name: {self.name}, Orders: {len(self.orders)})"
    
    def __repr__(self) -> str:
        """Developer representation of the customer."""
        return f"Customer({self.customer_id!r}, {self.name!r}, {self.address!r})"