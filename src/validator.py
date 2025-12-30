def validate_symbol(symbol):
    if not symbol.endswith("USDT"):
        raise ValueError("Only USDT pairs are allowed (example: BTCUSDT)")

def validate_quantity(quantity):
    try:
        qty = float(quantity)
    except ValueError:
        raise ValueError("Quantity must be a number")

    if qty <= 0:
        raise ValueError("Quantity must be greater than zero")

    return qty