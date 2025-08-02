def removeElement(nums, val):
    k = 0
    for i in range(len(nums)):
        if nums[i] != val:
            nums[k] = nums[i]
            k += 1
    return k

# nums = list(map(int, input("Enter the elements of the array (space-separated): ").split()))
# val = int(input("Enter the value to remove: "))


nums = [2, 3, 5, 4, 3, 7]
val = 3
k = removeElement(nums, val)
print(k)
print(nums[:k])