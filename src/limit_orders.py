import sys
from config import get_client
from logger import setup_logger
from validator import validate_symbol, validate_quantity

logger = setup_logger()

def validate_price(price):
    try:
        p = float(price)
    except ValueError:
        raise ValueError("Price must be a number")

    if p <= 0:
        raise ValueError("Price must be greater than zero")

    return p

def place_limit_order(symbol, side, quantity, price):
    try:
        validate_symbol(symbol)
        quantity = validate_quantity(quantity)
        price = validate_price(price)

        client = get_client()

        order = client.futures_create_order(
            symbol=symbol,
            side=side,
            type="LIMIT",
            quantity=quantity,
            price=price,
            timeInForce="GTC"
        )

        logger.info(f"Limit order placed | {order}")
        print("✅ Limit Order Placed Successfully")
        print(order)

    except Exception as error:
        logger.error(f"Limit order failed | {error}")
        print("❌ Error:", error)

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: python limit_orders.py <SYMBOL> <BUY/SELL> <QUANTITY> <PRICE>")
        sys.exit(1)

    _, symbol, side, quantity, price = sys.argv
    place_limit_order(symbol.upper(), side.upper(), quantity, price)