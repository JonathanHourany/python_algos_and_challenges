from ..get_max_profit import get_max_profit

def test_get_maxc_profit():
    stock_prices = [10, 7, 5, 8, 11, 9, 4, 7]
    assert get_max_profit(stock_prices) == 6