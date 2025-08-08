# def containsDuplicate(nums):
#     seen = set()

#     for num in nums:
#         if num in seen:
#             return True
#         seen.add(num)

#     return False

def containsDuplicate(nums):
    n = len(nums)
    for i in range(n - 1):
        for j in range(i + 1, n):
            if nums[i] == nums[j]:
                return True
    return False

nums = [1, 2, 3, 4 , 1]
print(containsDuplicate(nums))