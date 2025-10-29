from datetime import datetime
from typing import Optional

class Order:
    """
    Represents an order with complete order details.
    """
    
    def __init__(
        self,
        order_id: str,
        customer_id: str,
        item_sku: str,
        item_description: str,
        quantity: int,
        unit_price: float,
        order_date: Optional[datetime] = None
    ):
        """
        Initialize an Order instance.
        
        Args:
            order_id (str): Unique identifier for the order
            customer_id (str): Unique identifier for the customer
            item_sku (str): Stock keeping unit for the item
            item_description (str): Description of the item
            quantity (int): Number of items ordered
            unit_price (float): Price per unit
            order_date (datetime, optional): Date of the order. Defaults to current time.
        """
        self.order_id = order_id
        self.customer_id = customer_id
        self.order_date = order_date or datetime.now()
        self.item_sku = item_sku
        self.item_description = item_description
        self.quantity = quantity
        self.unit_price = unit_price
    
    @property
    def total_price(self) -> float:
        """Calculate and return the total price of the order."""
        return self.quantity * self.unit_price
    
    def __str__(self) -> str:
        """Return a string representation of the order."""
        return (f"Order {self.order_id}: {self.quantity}x {self.item_description} "
                f"(SKU: {self.item_sku}) at ${self.unit_price:.2f} each = ${self.total_price:.2f}")
    
    def __repr__(self) -> str:
        """Return a detailed representation of the order."""
        return (f"Order(order_id='{self.order_id}', customer_id='{self.customer_id}', "
                f"order_date={self.order_date}, item_sku='{self.item_sku}', "
                f"item_description='{self.item_description}', quantity={self.quantity}, "
                f"unit_price={self.unit_price}, total_price={self.total_price})")