def removeDuplicates(nums):
    k = 1
    for i in range(1, len(nums)):
        if nums[i] != nums[i - 1]:
            nums[k] = nums[i]
            k += 1
    return k

nums = [2, 6, 6, 7, 8]
nums.sort()
k = (removeDuplicates(nums))
print(k)
print(nums[:k])