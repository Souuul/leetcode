class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero_list = []
        one_list = []
        two_list = []

        for num in nums:
            if num == 0:
                zero_list.append(0)
            elif num == 1:
                one_list.append(1)
            else:
                two_list.append(2)
        for i, x in enumerate(zero_list+one_list+two_list):
            nums[i] = x
        return