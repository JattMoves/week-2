import numpy as np

names = np.array(['Hannah', 'Astrid', 'Abdul', 'Mauve', 'Jung'])
scores = np.array([99, 71, 85, 62, 91])
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
    min_score = np.min(scores)
    min_index = np.argmin(scores)
    return names[min_index], min_score

def sort_names(names, scores):
    sorted_indices = np.argsort(scores)
    sorted_names = names[sorted_indices]
    sorted_scores = scores[sorted_indices]
    return sorted_names, sorted_scores