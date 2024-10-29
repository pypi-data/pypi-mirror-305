import numpy as np
from ..base_indicator import BaseIndicator

class STOCHASTIC(BaseIndicator):
      def __init__(self):
            super().__init__("Stochastic")
            #self.period = period

      def calculate(param1, param2, high, low, close):
            high = np.array(high)
            low = np.array(low)
            close = np.array(close)
            n = len(close)
            
            lookback = int(param1 + 0.5)    # Lookback includes current bar
            n_to_smooth = int(param2 + 0.5) # Times to smooth; 1 for K, 2 for D
            front_bad = lookback - 1        # Number of undefined values at start

            output = np.full(n, 50.0)  # Initialize output with neutral value

            for i in range(front_bad, n):
                  window_high = high[i-lookback+1:i+1]
                  window_low = low[i-lookback+1:i+1]
                  
                  min_val = np.min(window_low)
                  max_val = np.max(window_high)
                  
                  sto_0 = (close[i] - min_val) / (max_val - min_val + 1e-60)
                  
                  if n_to_smooth == 0:
                        output[i] = 100.0 * sto_0
                  elif n_to_smooth == 1:
                        if i == front_bad:
                              sto_1 = sto_0
                        else:
                              sto_1 = 0.33333333 * sto_0 + 0.66666667 * sto_1
                        output[i] = 100.0 * sto_1
                  else:  # n_to_smooth == 2
                        if i == front_bad:
                              sto_1 = sto_0
                              sto_2 = sto_1
                        elif i == front_bad + 1:
                              sto_1 = 0.33333333 * sto_0 + 0.66666667 * sto_1
                              sto_2 = sto_1
                        else:
                              sto_1 = 0.33333333 * sto_0 + 0.66666667 * sto_1
                              sto_2 = 0.33333333 * sto_1 + 0.66666667 * sto_2
                        output[i] = 100.0 * sto_2

            return output