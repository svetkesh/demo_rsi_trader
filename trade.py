import alpaca_trade_api as tradeapi
from alpaca_trade_api.rest import APIError

def trade_via_alpaca(
    apca_api_key_id,
    apca_api_secter_key,
    apca_api_base_url,
    symbol,
    side,
    api_version='v2',
    qty=1,
    type='market',
    time_in_force='gtc'
):
    api = tradeapi.REST(
        apca_api_key_id,
        apca_api_secter_key,
        base_url=apca_api_base_url,
        api_version=api_version
    )
    try:
        api.submit_order(
            symbol=symbol,
            qty=qty,
            side=side,
            type=type,                   # 'market', etc
            time_in_force=time_in_force  #'gtc', etc
        )
        return None
    except APIError as api_err:
        return api_err
