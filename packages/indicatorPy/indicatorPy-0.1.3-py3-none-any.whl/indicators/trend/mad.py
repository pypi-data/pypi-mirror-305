import numpy as np
from scipy import stats
from ..base_indicator import BaseIndicator
from ..common.common import CommonMethods

class MA_DIFFERENCE(BaseIndicator):
      
      def __init__(self):
            super().__init__("Moving Average Difference")
            #self.period = period

        # def atr(open_prices, high, low, close, length):
        #     high_low = high - low
        #     high_close = np.abs(high - np.roll(close, 1))
        #     low_close = np.abs(low - np.roll(close, 1))
            
        #     ranges = np.max([high_low, high_close, low_close], axis=0)
        #     return np.convolve(ranges, np.ones(length)/length, mode='valid')

      def calculate(self,param1, param2, param3, data):

            open = np.array(data['open'])
            high = np.array(data['high'])
            low = np.array(data['low'])
            close = np.array(data['close'])
            n = len(close)
            
            short_length = int(param1 + 0.5)
            long_length = int(param2 + 0.5)
            lag = int(param3 + 0.5)
            front_bad = min(long_length + lag, n)

            output = np.zeros(n)

            # Compute ATR for the entire series
            atr_values = CommonMethods.atr(open, high, low, close, long_length + lag)

            for icase in range(front_bad, n):
                # Compute long-term moving average
                long_sum = np.sum(close[icase-long_length-lag+1:icase-lag+1])
                long_ma = long_sum / long_length

                # Compute short-term moving average
                short_sum = np.sum(close[icase-short_length+1:icase+1])
                short_ma = short_sum / short_length

                # Compute the normalizing factor
                diff = 0.5 * (long_length - 1.0) + lag - 0.5 * (short_length - 1.0)
                denom = np.sqrt(np.abs(diff)) * atr_values[icase - front_bad]

                ma_diff = (short_ma - long_ma) / (denom + 1e-60)
                output[icase] = 100.0 * stats.norm.cdf(1.5 * ma_diff) - 50.0

            return output