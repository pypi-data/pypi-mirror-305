import numpy as np
from ..base_indicator import BaseIndicator

class STOCHASTIC_RSI(BaseIndicator):
      def __init__(self):
            super().__init__("Stochastic RSI")
            #self.period = period
      def calculate_stochastic_rsi(param1, param2, param3, close):
            close = np.array(close)
            n = len(close)
            
            lookback = int(param1 + 0.5)      # RSI lookback
            lookback2 = int(param2 + 0.5)     # Stochastic lookback
            n_to_smooth = int(param3 + 0.5)   # Lookback for final exponential smoothing

            front_bad = lookback + lookback2 - 1  # Number of undefined values at start

            output = np.full(n, 50.0)  # Initialize output with neutral value
            work1 = np.zeros(n)  # For storing RSI values

            # Compute RSI
            diff = np.diff(close)
            gains = np.maximum(diff, 0)
            losses = -np.minimum(diff, 0)
            
            avg_gain = np.sum(gains[:lookback-1]) / (lookback - 1)
            avg_loss = np.sum(losses[:lookback-1]) / (lookback - 1)

            for i in range(lookback, n):
                  avg_gain = ((lookback - 1) * avg_gain + gains[i-1]) / lookback
                  avg_loss = ((lookback - 1) * avg_loss + losses[i-1]) / lookback
                  rs = avg_gain / (avg_loss + 1e-60)
                  work1[i] = 100 - (100 / (1 + rs))

            # Compute Stochastic RSI
            for i in range(front_bad, n):
                  window = work1[i-lookback2+1:i+1]
                  min_val = np.min(window)
                  max_val = np.max(window)
                  output[i] = 100.0 * (work1[i] - min_val) / (max_val - min_val + 1e-60)

            # Smooth if requested
            if n_to_smooth > 1:
                  alpha = 2.0 / (n_to_smooth + 1.0)
                  smoothed = output[front_bad]
                  for i in range(front_bad+1, n):
                        smoothed = alpha * output[i] + (1.0 - alpha) * smoothed
                        output[i] = smoothed

            return output