import numpy as np
from scipy import stats
from ..base_indicator import BaseIndicator
from ..common.common import CommonMethods

class MACD(BaseIndicator):
      
      def __init__(self):
            super().__init__("Moving Average Convergence Divergence")
            #self.period = period

      def calculate(self, param1, param2, param3, data):
            open_prices = np.array(data['open'])
            high = np.array(data['high'])
            low = np.array(data['low'])
            close = np.array(data['close'])
            n = len(close)
            
            short_length = int(param1 + 0.5)
            long_length = int(param2 + 0.5)
            n_to_smooth = int(param3 + 0.5)

            long_alpha = 2.0 / (long_length + 1.0)
            short_alpha = 2.0 / (short_length + 1.0)

            output = np.zeros(n)
            long_sum = short_sum = close[0]
            
            # Compute ATR for the entire series
            atr_values = np.concatenate([np.zeros(long_length + n_to_smooth - 1), 
                                        CommonMethods.atr(open_prices, high, low, close, long_length + n_to_smooth)])

            for icase in range(1, n):
                # Compute long-term and short-term exponential smoothing
                long_sum = long_alpha * close[icase] + (1.0 - long_alpha) * long_sum
                short_sum = short_alpha * close[icase] + (1.0 - short_alpha) * short_sum

                # Compute the normalizing factor
                diff = 0.5 * (long_length - 1.0) - 0.5 * (short_length - 1.0)
                denom = np.sqrt(np.abs(diff)) * atr_values[icase]

                macd = (short_sum - long_sum) / (denom + 1e-15)
                output[icase] = 100.0 * stats.norm.cdf(1.0 * macd) - 50.0

            # Smooth and compute differences if requested
            if n_to_smooth > 1:
                alpha = 2.0 / (n_to_smooth + 1.0)
                smoothed = output[0]
                for icase in range(1, n):
                    smoothed = alpha * output[icase] + (1.0 - alpha) * smoothed
                    output[icase] -= smoothed

            return output