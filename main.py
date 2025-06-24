from dotenv import load_dotenv
load_dotenv()

from config import API_KEY, API_SECRET
from bot import BasicBot
from utils import validate_order_input
from logger import setup_logger

def main():
    setup_logger()
    bot = BasicBot(API_KEY, API_SECRET)

    print("Welcome to the Binance Futures Testnet Trading Bot")

    symbol = input("Enter symbol (e.g., BTCUSDT): ").upper()
    side = input("Enter side (BUY/SELL): ").upper()
    order_type = input("Enter order type (MARKET/LIMIT/STOP_LIMIT/STOP_MARKET): ").upper()
    quantity = float(input("Enter quantity: "))

    price = None
    stop_price = None

    if order_type in ['LIMIT', 'STOP_LIMIT']:
        price = float(input("Enter limit price: "))

    if order_type in ['STOP_MARKET', 'STOP_LIMIT']:
        stop_price = float(input("Enter stop price: "))

    if not validate_order_input(symbol, side, order_type, quantity, price):
        print("Invalid input. Please check and try again.")
        return

    order = bot.place_order(symbol, side, order_type, quantity, price, stop_price)
    if order:
        print(f"✅ Order placed successfully:\n{order}")
    else:
        print("❌ Order failed. Check logs for details.")

if __name__ == "__main__":
    main()