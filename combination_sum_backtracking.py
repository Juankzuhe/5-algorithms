""" Given a set of candidate numbers (candidates) (without duplicates) """

def combination_sum(candidates, target):
    """ Given a set of candidate numbers (candidates) (without duplicates) 
        and a target number (target), find all unique combinations in 
        candidates where the candidate numbers sums to target.  The same repeated
        number may be chosen from candidates unlimited number of times. """
    answer = []

    def combination_sum_helper(
        candidates, current_index, current_sum, current_combination, target
    ):
        if current_sum == target:
            answer.append(current_combination)
            return
        if current_sum > target:
            return
        for i in range(current_index, len(candidates)):
            combination_sum_helper(
                candidates,
                i,
                current_sum + candidates[i],
                current_combination + [candidates[i]],
                target,
            )

    combination_sum_helper(candidates, 0, 0, [], target)
    return answer


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
