from binance.client import Client

# 🔐 Binance Futures Testnet API keys
API_KEY = "Q6Kws9sZ3xrT5VlszQhwBSDxv5hcn2ztlfXI6J9upOhe3hWHlkVw7aUCEwacc5Bu"
API_SECRET = "lsUJ22WwdTnHI0RUApCf3ni2aWuEA0K8t6ZHRCyzsTng6SBF1OERssK3sphufZLN"

# 🌐 Testnet client setup
def get_client():
    client = Client(API_KEY, API_SECRET)
    client.FUTURES_URL = "https://testnet.binancefuture.com"
    return client