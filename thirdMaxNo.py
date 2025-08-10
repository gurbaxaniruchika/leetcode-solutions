def thirdMax(nums):
    nums = list(set(nums))
    if len(nums) < 3:
        return max(nums)
    nums.sort(reverse = True)
    return nums[2]

print(thirdMax([3, 2, 1]))