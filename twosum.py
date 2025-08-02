def twoSum(nums, target):
    n = len(nums)
    for i in range(n-1):
        for j in range(i + 1, n):
            if nums[i] + nums[j] == target:
                return [i, j]
    return []

nums = [5,9,8,7,2]
target = 9
print(twoSum(nums, target))