class NumArray:
    def __init__(self, nums):
        self.prefix_sum = [0]
        for num in nums:
            self.prefix_sum.append(self.prefix_sum[-1] + num)
    def sumRange(self, left, right):
        return self.prefix_sum[right + 1] - self.prefix_sum[left]
    
nums = [-2, 0, 3, -5, 2, -1]
obj = NumArray(nums)
print(obj.sumRange(0, 2))   #1
print(obj.sumRange(2, 5))   #-1
print(obj.sumRange(0, 5))   #-3