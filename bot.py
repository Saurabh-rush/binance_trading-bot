from binance.client import Client
from binance.exceptions import BinanceAPIException
from config import BASE_URL
import logging

class BasicBot:
    
        
    def __init__(self, api_key, api_secret, testnet=True):
        if testnet:
            Client.FUTURES_URL = "https://testnet.binancefuture.com"  # ✅ globally override the futures URL

        self.client = Client(api_key, api_secret)
        self.logger = logging.getLogger("TradingBot")


    def place_order(self, symbol, side, order_type, quantity, price=None, stop_price=None):
        try:
            self.logger.info(f"Placing Order | Symbol: {symbol}, Side: {side}, Type: {order_type}, Qty: {quantity}, Price: {price}, Stop: {stop_price}")
            print(f"\n🔁 Placing Order: {order_type} {side} {quantity} {symbol}...\n")

            if order_type == 'MARKET':
                order = self.client.futures_create_order(
                    symbol=symbol,
                    side=side,
                    type='MARKET',
                    quantity=quantity
                )

            elif order_type == 'LIMIT':
                order = self.client.futures_create_order(
                    symbol=symbol,
                    side=side,
                    type='LIMIT',
                    quantity=quantity,
                    price=price,
                    timeInForce='GTC'
                )

            elif order_type == 'STOP_MARKET':
                order = self.client.futures_create_order(
                    symbol=symbol,
                    side=side,
                    type='STOP_MARKET',
                    stopPrice=stop_price,
                    quantity=quantity,
                    timeInForce='GTC'
                )

            elif order_type == 'STOP_LIMIT':
                order = self.client.futures_create_order(
                    symbol=symbol,
                    side=side,
                    type='STOP',
                    stopPrice=stop_price,
                    price=price,
                    quantity=quantity,
                    timeInForce='GTC'
                )

            else:
                raise ValueError(f"❌ Unsupported order type: {order_type}")

            self.logger.info(f"✅ Order Response: {order}")
            return order

        except BinanceAPIException as e:
            # print(f"❌ BinanceAPIException: {e}")
            # self.logger.error(f"API Error: {e.status_code} - {e.message} - {e.response.text}")
            return None

        except Exception as e:
            # print(f"❌ Unexpected Error: {e}")
            # self.logger.error(f"Unexpected Error: {str(e)}")
            return None