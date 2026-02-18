def survival_probability(bankroll, bet, edge, odds):
    import math
    return math.exp(-2 * bet * edge / odds)
