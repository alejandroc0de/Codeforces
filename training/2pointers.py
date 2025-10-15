#Squares of a sorted array, return array increasing
nums = [-4,-1,0,3,10]
left = 0
right = len(nums)-1
result = []

while left<=right:
    if(abs(nums[left]) > abs(nums[right])):
        result.append(nums[left]**2) # Insert takes O(n), append O(1)
        left = left + 1 # We move the pointer
    else:
        result.append(nums[right]**2)
        right = right - 1
result.reverse()
print(result)
