
def intersection(nums):
    new_set = set(nums[0])
    for i in range(1, len(nums)):
        new_set &= set(nums[i])
    new_set = list(new_set)
    new_set.sort()
    return new_set

array = [[3,1,2,4,5],[1,2,3,4],[3,4,5,6]]

print(intersection(array))
