import sys
from config import get_client
from logger import setup_logger
from validator import validate_symbol, validate_quantity

logger = setup_logger()

def place_market_order(symbol, side, quantity):
    try:
        # Input validation
        validate_symbol(symbol)
        quantity = validate_quantity(quantity)

        client = get_client()

        order = client.futures_create_order(
            symbol=symbol,
            side=side,
            type="MARKET",
            quantity=quantity
        )

        logger.info(f"Market order placed | {order}")
        print("✅ Market Order Success")
        print(order)

    except Exception as error:
        logger.error(f"Market order failed | {error}")
        print("❌ Error:", error)

if __name__ == "__main__":
    # CLI arguments
    if len(sys.argv) != 4:
        print("Usage: python market_orders.py <SYMBOL> <BUY/SELL> <QUANTITY>")
        sys.exit(1)

    _, symbol, side, quantity = sys.argv
    place_market_order(symbol.upper(), side.upper(), quantity)