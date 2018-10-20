# daily problem 1
# given a list of integers check whether any 2 of them sum to an integer k

# k = 17
# nums = [1, 2, 3, 4, 5, 6, 10, 8, 9]

k = 22
nums = [95, 90, 5, 17, 40, 22, 88, 50, 1]

# n^2 implementation
def list(k , nums):
    for i in nums:
        for j in nums: 
            if (i+j == k):
                return True
    return False

# n log n + n implementation
# creating 2 pointers which run through a sorted list
# sorting takes n log n time
# starts off checking the smallest + largest 
# moves to a larger smallest or a smaller largest depending on result
def list2(k, nums):
    nums.sort()
    first = 0
    last = len(nums) - 1
    while (first <= last):
        num_sum = nums[first] + nums[last]
        if (num_sum < k):
            first += 1
        elif (num_sum > k):
            last -= 1
        else:
            return True
    return False

print(list2(k, nums))