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


def sort_name(names, scores):
    name_score_pairs = list(zip(names, scores))
    sorted_pairs = sorted(name_score_pairs, key=lambda x: x[1], reverse=True)
    sorted_names = [pair[0] for pair in sorted_pairs]
    sorted_scores = [pair[1] for pair in sorted_pairs]
    return sorted_names, sorted_scores
