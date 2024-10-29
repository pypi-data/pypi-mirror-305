import numpy as np
from ..base_indicator import BaseIndicator

class DETRENDED_RSI(BaseIndicator):
      def __init__(self):
            super().__init__("Detrended RSI")
            #self.period = period

      def calculate(self, param1, param2, param3, close):
            close = np.array(close)
            n = len(close)
            short_length = int(param1 + 0.5)  # RSI being detrended
            long_length = int(param2 + 0.5)   # Detrender (greater than short_length)
            length = int(param3 + 0.5)        # Lookback for linear fit (as long as reasonably possible)
            front_bad = long_length + length - 1  # Number of undefined values at start

            output = np.zeros(n)
            work1 = np.full(n, 1e90)
            work2 = np.full(n, -1e90)

            # Calculate differences
            diff = np.diff(close)

            # Initialize short (detrended) RSI
            upsum = np.sum(np.maximum(diff[:short_length-1], 0))
            dnsum = -np.sum(np.minimum(diff[:short_length-1], 0))
            upsum, dnsum = upsum / (short_length - 1), dnsum / (short_length - 1)

            for icase in range(short_length, n):
                  d = diff[icase-1]
                  if d > 0:
                        upsum = ((short_length - 1.0) * upsum + d) / short_length
                        dnsum *= (short_length - 1.0) / short_length
                  else:
                        dnsum = ((short_length - 1.0) * dnsum - d) / short_length
                        upsum *= (short_length - 1.0) / short_length
                  work1[icase] = 100.0 * upsum / (upsum + dnsum)

            if short_length == 2:
                  mask = np.arange(n) >= short_length
                  work1[mask] = -10.0 * np.log(2.0 / (1 + 0.00999 * (2 * work1[mask] - 100)) - 1)

            # Initialize long (detrender) RSI
            upsum = np.sum(np.maximum(diff[:long_length-1], 0))
            dnsum = -np.sum(np.minimum(diff[:long_length-1], 0))
            upsum, dnsum = upsum / (long_length - 1), dnsum / (long_length - 1)

            for icase in range(long_length, n):
                  d = diff[icase-1]
                  if d > 0:
                        upsum = ((long_length - 1.0) * upsum + d) / long_length
                        dnsum *= (long_length - 1.0) / long_length
                  else:
                        dnsum = ((long_length - 1.0) * dnsum - d) / long_length
                        upsum *= (long_length - 1.0) / long_length
                  work2[icase] = 100.0 * upsum / (upsum + dnsum)

            # Process detrended RSI
            for icase in range(front_bad, n):
                  slice_work1 = work1[icase-length+1:icase+1]
                  slice_work2 = work2[icase-length+1:icase+1]

                  xmean = np.mean(slice_work2)
                  ymean = np.mean(slice_work1)

                  xdiff = slice_work2 - xmean
                  ydiff = slice_work1 - ymean

                  coef = np.sum(xdiff * ydiff) / (np.sum(xdiff**2) + 1e-60)

                  output[icase] = ydiff[-1] - coef * xdiff[-1]

            return output