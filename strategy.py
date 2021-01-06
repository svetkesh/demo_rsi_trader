from alpha_vantage.techindicators import TechIndicators


def get_action_action_for_symbol(
        av_api_key,
        symbol,
        rsi_buy_below=30,
        rsi_sell_above=70):

    try:
        ti = TechIndicators(av_api_key)
        aapl_rsi, aapl_meta_rsi = ti.get_rsi(symbol=symbol)
        last_date = sorted(aapl_rsi)[-1]
        last_rsi_value = eval(aapl_rsi.get(last_date).get('RSI'))

        print(f'get_action_action_for_symbol {symbol}, {last_date} RSI={last_rsi_value} ')

        if last_rsi_value > rsi_sell_above:
            return 'sell'
        elif last_rsi_value < rsi_buy_below:
            return 'buy'
        else:
            return None
    except ValueError as av_api_err:
        print(f'Error get TechIndicators for {symbol}: {type(av_api_err), av_api_err}')
        return None


