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

def lowest_score(names, scores):
    return names[np.argmin(scores)]


def sort_names(names, scores):
    sorted_names = list(names)
    sorted_scores = list(scores)

    for i in range(len(sorted_scores)):
        for j in range(i + 1, len(sorted_scores)):
            if sorted_scores[j] > sorted_scores[i]:
                sorted_scores[i], sorted_scores[j] = sorted_scores[j], sorted_scores[i]
                sorted_names[i], sorted_names[j] = sorted_names[j], sorted_names[i]

    return sorted_names