def searchInsert(nums, target):
    left = 0
    right = len(nums) - 1
    while left <= right:
        mid = (left + right) // 2

        if nums[mid] == target:
            return target
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return left
    
nums = [2, 4, 6, 1, 9]
target = 5
print(searchInsert(nums, target))