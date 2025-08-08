def containsDuplicate(nums, k):
    last_seen = {}

    for i in range(len(nums)):
        num = nums[i]
        if num in last_seen and i - last_seen[num] <= k:
            return True
        last_seen[num] = i
    return False

nums = [1, 2, 3, 1]
k = 3
print(containsDuplicate(nums, k))