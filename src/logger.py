import logging
import os

def setup_logger():
    logger = logging.getLogger("binance_bot")
    logger.setLevel(logging.INFO)

    log_file = os.path.join(os.getcwd(), "..", "bot.log")

    if not logger.handlers:
        file_handler = logging.FileHandler(log_file)
        formatter = logging.Formatter(
            "%(asctime)s | %(levelname)s | %(message)s"
        )
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

    return logger