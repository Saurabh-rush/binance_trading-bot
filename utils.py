def validate_order_input(symbol, side, order_type, quantity, price=None):
    if not symbol or side not in ['BUY', 'SELL']:
        return False
    if order_type not in ['MARKET', 'LIMIT', 'STOP_LIMIT', 'STOP_MARKET']:
        return False
    if quantity <= 0:
        return False
    if order_type in ['LIMIT', 'STOP_LIMIT'] and (price is None or float(price) <= 0):
        return False
    return True