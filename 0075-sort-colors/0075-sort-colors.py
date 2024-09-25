class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero_pt = 0
        one_pt = 0
        two_pt = 0
        for num in nums:
            if num == 0:
                zero_pt += 1
            elif num == 1:
                one_pt += 1
            else:
                two_pt += 1

        for i in range(zero_pt):
            nums[i] = 0

        for i in range(zero_pt, zero_pt+one_pt):
            nums[i] = 1

        for i in range(zero_pt+one_pt, zero_pt+one_pt+two_pt):
            nums[i] = 2
        return