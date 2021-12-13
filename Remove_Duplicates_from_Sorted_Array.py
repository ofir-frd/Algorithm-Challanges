"""
Remove Duplicates from Sorted Array:
Not allowed to allocate extra space for another array
"""

def removeDuplicates(nums: list):
    i=0
    while i < (len(nums) - 1):
        if nums[i] == nums[i + 1]:
            nums.pop(i)
            continue
        i += 1

    print(nums)   
    return len(nums)
