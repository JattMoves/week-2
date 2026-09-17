import numpy as np


# update/add code below ...

def ways(n):
    """Calculates the number of ways to make change for n cents using pennies and nickels."""
    num_pennies = 1
    num_nickels = 5

    total_ways = 0
    for pennies in range(n // num_pennies + 1):
        for nickels in range(n // num_nickels + 1):
            if pennies * num_pennies + nickels * num_nickels == n:
                total_ways += 1
    return (total_ways)

def lowest_score(names, scores):
    """Returns the name of the person with the lowest score."""
    return names[np.argmin(scores)]


def sort_names(names, scores):
    """Sorts and returns names in descending order based on their corresponding scores."""
    sorted_names = list(names)
    sorted_scores = list(scores)

    for i in range(len(sorted_scores)):
        for j in range(i + 1, len(sorted_scores)):
            if sorted_scores[j] > sorted_scores[i]:
                sorted_scores[i], sorted_scores[j] = sorted_scores[j], sorted_scores[i]
                sorted_names[i], sorted_names[j] = sorted_names[j], sorted_names[i]

    return sorted_names
