def get_order(order):
    if not order.get('items') or not isinstance(order['items'], list):
        raise ValueError("Order must contain a list of items.")
    
    if len(order['items']) == 0:
        raise ValueError("Order must contain at least one item.")
    
    return True
