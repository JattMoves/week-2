import numpy as np


# update/add code below ...

def ways(n):
    num_pennies = 1
    num_nickels = 5

    total_ways = 0
    for pennies in range(n // num_pennies + 1):
        for nickels in range(n // num_nickels + 1):
            if pennies * num_pennies + nickels * num_nickels == n:
                total_ways += 1
                snap = (([pennies, nickels]))
                print(snap)
    return (total_ways)

from tkinter.font import names


def lowest_score(names, scores):
    return names[np.argmin(scores)]


def sort_names(names, scores):
    name_score_pairs = zip(names, scores)
    sorted_pairs = sorted(name_score_pairs, key=lambda pair: pair[1], reverse=True)
    return [name for name, score in sorted_pairs]