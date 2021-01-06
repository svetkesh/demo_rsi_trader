import os

from dotenv import load_dotenv

from strategy import get_action_action_for_symbol
from trade import trade_via_alpaca
from load_symbols import get_symbols

load_dotenv()

# key for datasource API
av_api_key = os.getenv("ALPHA_VANTAGE_API_KEY")

# keys for trading API
apca_api_key_id = os.getenv("APCA_API_KEY_ID")
apca_api_secter_key = os.getenv("APCA_API_SECRET_KEY")

# path for real or 'paper' money
apca_api_base_url = os.getenv("APCA_API_BASE_URL")

# RSI strategy threshold
rsi_buy_below = eval(os.getenv("RSI_BUY_BELOW"))
rsi_sell_above = eval(os.getenv("RSI_SELL_ABOVE"))


symbols = get_symbols()
for symbol in symbols:
    action_for_symbol = get_action_action_for_symbol(
        av_api_key,
        symbol=symbol,
        rsi_buy_below=rsi_buy_below,
        rsi_sell_above=rsi_sell_above,
    )

    print(action_for_symbol)

    if action_for_symbol:
        trade_result = trade_via_alpaca(
            apca_api_key_id=apca_api_key_id,
            apca_api_secter_key=apca_api_secter_key,
            apca_api_base_url=apca_api_base_url,
            symbol=symbol,
            side=action_for_symbol
        )
        if trade_result:
            print(f'Failed {type(trade_result), trade_result}')
        else:
            print(f'Success for {symbol}')

print('done')
