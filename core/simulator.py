import numpy as np
from core.crash_math import crash_outcome
from core.mines_math import mines_outcome
from core.bayesian_edge import BayesianEdge

def run_crash_sim(rounds):
    edge_calc = BayesianEdge()
    history = []

    balance = 1.0
    for _ in range(rounds):
        win, payout = crash_outcome()
        edge_calc.update(win)

        balance += payout - 1
        history.append(balance)

    return history, edge_calc.estimate()

def run_mines_sim(rounds):
    edge_calc = BayesianEdge()
    history = []

    balance = 1.0
    for _ in range(rounds):
        win, payout = mines_outcome()
        edge_calc.update(win)

        balance += payout - 1
        history.append(balance)

    return history, edge_calc.estimate()
