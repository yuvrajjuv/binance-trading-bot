import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from config import get_client
from logger import setup_logger
from validator import validate_symbol, validate_quantity

logger = setup_logger()

def validate_price(value, name):
    try:
        v = float(value)
    except ValueError:
        raise ValueError(f"{name} must be a number")

    if v <= 0:
        raise ValueError(f"{name} must be greater than zero")

    return v

def place_stop_limit(symbol, side, quantity, stop_price, limit_price):
    try:
        validate_symbol(symbol)
        quantity = validate_quantity(quantity)
        stop_price = validate_price(stop_price, "Stop price")
        limit_price = validate_price(limit_price, "Limit price")

        client = get_client()

        order = client.futures_create_order(
            symbol=symbol,
            side=side,
            type="STOP",
            quantity=quantity,
            price=limit_price,
            stopPrice=stop_price,
            timeInForce="GTC"
        )

        logger.info(f"Stop-Limit order placed | {order}")
        print("✅ Stop-Limit Order Placed Successfully")
        print(order)

    except Exception as error:
        logger.error(f"Stop-Limit order failed | {error}")
        print("❌ Error:", error)

if __name__ == "__main__":
    if len(sys.argv) != 6:
        print(
            "Usage: python stop_limit.py <SYMBOL> <BUY/SELL> <QTY> <STOP_PRICE> <LIMIT_PRICE>"
        )
        sys.exit(1)

    _, symbol, side, qty, stop_p, limit_p = sys.argv
    place_stop_limit(symbol.upper(), side.upper(), qty, stop_p, limit_p)