import numpy as np

def crash_outcome():
    crash_point = np.random.exponential(1.5)
    win = crash_point > 2.0
    payout = crash_point if win else 0
    return win, payout
