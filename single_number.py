from sets import Set


# without space
def single_number(nums):
    result = 0
    for i in nums:
        result ^= i
    return result


# with more space
def single_number2(nums):
    marked = Set()
    for i in nums:
        if i in marked:
            marked.remove(i)
        else:
            marked.add(i)
    for i in marked:
        return i


print single_number([1,2,4,5,1,2,5])