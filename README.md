# Binance Futures Trading Bot (Testnet)

This project is a Python-based trading bot developed using the Binance Futures *Testnet API*.
It supports multiple order types via command-line interface and follows a clean, modular structure.

---

## 📁 Project Structure

binance_bot/
│
├── src/
│   ├── config.py            # API configuration & client setup
│   ├── logger.py            # Logging configuration
│   ├── validator.py         # Input validation utilities
│   ├── market_orders.py     # Market order implementation
│   ├── limit_orders.py      # Limit order implementation
│   └── advanced/
│       └── stop_limit.py    # Stop-Limit order implementation
│
├── bot.log                  # Application logs
├── README.md
└── report.pdf               # Detailed explanation & screenshots