from typing import List

def get_max_profit(stock_prices: List[int]) -> int:
    min_price = float('inf')
    buy_sell_deltas = []

    for stock_price in stock_prices:
        if stock_price < min_price:
            min_price = stock_price
        buy_sell_deltas.append(stock_price - min_price)

    return max(buy_sell_deltas)
