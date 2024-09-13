class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def target_meet_combination_sum(candidates, target, combination_list = [], answer = [], start=0):
            if target == 0:
                answer.append(combination_list.copy())
                return
            if target < 0:
                return
            for index in range(start, len(candidates)):
                combination_list.append(candidates[index])
                target_meet_combination_sum(candidates, target-candidates[index], combination_list, answer, index)
                combination_list.pop()
            return answer
        return target_meet_combination_sum(candidates, target)