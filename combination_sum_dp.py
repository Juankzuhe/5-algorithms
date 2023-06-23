""" Combination sum problem using dynamic programming """


def combination_sum(candidates, target):
    """Given a set of candidate numbers (candidates) (without duplicates)"""
    dp = [[] for i in range(target + 1)]
    dp[0].append([])

    for candidate in candidates:
        for i in range(1, target + 1):
            if i - candidate >= 0:
                for combination in dp[i - candidate]:
                    dp[i].append(combination + [candidate])

    return dp[-1]


candidates = [2, 3, 6, 7]
target = 7
print(combination_sum(candidates, target))
candidates = [2, 3, 5]
target = 8
print(combination_sum(candidates, target))
candidates = [2]
target = 1
print(combination_sum(candidates, target))
candidates = [1]
target = 1
print(combination_sum(candidates, target))
candidates = [1]
target = 2
print(combination_sum(candidates, target))
