nums = [-1, 0, 3, 5, 9, 12,34,56,78,89,99,123,134,145,156,167,177,200,210,213,215]
target = 145



m = 0


def getIndex():
    l = 0
    r = len(nums)-1
    while l <= r :
        m = (l+r)//2
        if(nums[m]==target):
            return m
        elif(target<nums[m]):
            r = m-1
        else:
            l = m + 1
    return -1

getIndex()