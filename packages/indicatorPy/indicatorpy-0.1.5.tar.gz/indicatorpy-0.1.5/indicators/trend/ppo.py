import numpy as np
from scipy import stats
from ..base_indicator import BaseIndicator

class PPO(BaseIndicator):
      
      def __init__(self):
            super().__init__("Percentage Price Oscillator")
            #self.period = period

      def calculate(self,param1, param2, param3, close):
            close = np.array(close)
            n = len(close)
            
            short_length = int(param1 + 0.5)
            long_length = int(param2 + 0.5)
            n_to_smooth = int(param3 + 0.5)

            long_alpha = 2.0 / (long_length + 1.0)
            short_alpha = 2.0 / (short_length + 1.0)

            output = np.zeros(n)
            long_sum = short_sum = close[0]

            for icase in range(1, n):
                # Compute long-term and short-term exponential smoothing
                long_sum = long_alpha * close[icase] + (1.0 - long_alpha) * long_sum
                short_sum = short_alpha * close[icase] + (1.0 - short_alpha) * short_sum
                
                # Calculate the 'official' PPO
                output[icase] = 100.0 * (short_sum - long_sum) / (long_sum + 1e-15)
                
                # Normalize to reduce outliers
                output[icase] = 100.0 * stats.norm.cdf(0.2 * output[icase]) - 50.0

            # Smooth and compute differences if requested
            if n_to_smooth > 1:
                alpha = 2.0 / (n_to_smooth + 1.0)
                smoothed = output[0]
                for icase in range(1, n):
                    smoothed = alpha * output[icase] + (1.0 - alpha) * smoothed
                    output[icase] -= smoothed

            return output