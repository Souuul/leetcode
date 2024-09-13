class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        def find_combinations(candidates, target, start=0, current_combination=[], answer=[]):
            if target == 0:
                answer.append(current_combination.copy())
                return
            if target < 0:
                return

            for i in range(start, len(candidates)):
                current_combination.append(candidates[i])
                find_combinations(candidates, target - candidates[i], i, current_combination, answer)
                current_combination.pop()

            return answer


        # 1. 후보군에서 목표와 같은 값이 있는지 확인
        answer = []
        for candidate in candidates:
            if candidate == target:
                answer.append([candidate])

        # 2. 재귀를 사용하여 조합 찾기
        result = find_combinations(candidates, target)
        return(result)
        