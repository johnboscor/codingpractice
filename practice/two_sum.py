def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    temp = []
    for i in range(len(nums)):
        if nums[i] in temp:
            return [temp.index(nums[i]), i]
        temp.append(abs(nums[i] - target))

A=[6,6]
target=12
print(twoSum(A,target))