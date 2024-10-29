import numpy as np
from scipy import stats

def legendre_3(n):
    x = np.linspace(-1, 1, n)
    return (x, 0.5 * (3 * x**2 - 1), 0.5 * (5 * x**3 - 3 * x))

def atr(open_prices, high, low, close, length):
    high_low = high - low
    high_close = np.abs(high - np.roll(close, 1))
    low_close = np.abs(low - np.roll(close, 1))
    
    ranges = np.max([high_low, high_close, low_close], axis=0)
    return np.convolve(ranges, np.ones(length)/length, mode='valid')

def calculate_polynomial_trend(var_num, param1, param2, open_prices, high, low, close):
    pass