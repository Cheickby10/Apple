import numpy as np

def mines_outcome():
    cells = 25
    mines = 3
    safe_spots = cells - mines

    pos = np.random.randint(0, cells)
    win = pos >= mines
    payout = safe_spots / cells if win else 0
    return win, payout
