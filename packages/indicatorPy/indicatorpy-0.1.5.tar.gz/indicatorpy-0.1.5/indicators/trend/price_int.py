import numpy as np
from ..base_indicator import BaseIndicator
from scipy import stats

      
class PRICE_INT(BaseIndicator):
      def __init__(self):
            super().__init__("Price intensity")


      def calculate(self, param1, data):
            open_prices, high, low, close = map(np.array, (data['open'], data['high'], data['low'], data['close']))
            n = len(close)
            
            n_to_smooth = max(int(param1 + 0.5), 1)
            output = np.zeros(n)
            
            # Calculate first bar
            denom = max(high[0] - low[0], 1e-60)
            output[0] = (close[0] - open_prices[0]) / denom
            
            # Calculate raw values for remaining bars
            for i in range(1, n):
                  denom = high[i] - low[i]
                  denom = max(denom, high[i] - close[i-1])
                  denom = max(denom, close[i-1] - low[i])
                  denom = max(denom, 1e-60)
                  output[i] = (close[i] - open_prices[i]) / denom
            
            # Apply exponential smoothing if requested
            if n_to_smooth > 1:
                  alpha = 2.0 / (n_to_smooth + 1.0)
                  smoothed = output[0]
                  for i in range(1, n):
                        smoothed = alpha * output[i] + (1.0 - alpha) * smoothed
                        output[i] = smoothed
            
            # Final transformation and mild compression
            output = 100.0 * stats.norm.cdf(0.8 * np.sqrt(n_to_smooth) * output) - 50.0
            
            return output
                  