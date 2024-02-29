# Function to find the all possible permutations
def permutations(res, nums, l, h):
    if l == h:
        res.append(nums[:])
        return
    for i in range(l, h+1):
        nums[l], nums[i] = nums[i], nums[l]
        permutations(res, nums, l+1,h)
        nums[l], nums[i] = nums[i], nums[l]


# Function to get the all possible permutations
def permute(nums):
    res = []
    x = len(nums)-1
    permutations(res, nums, 0, x)
    return res


nums = [1,2,4]
res = permute(nums)
s = set()
for x in res:
    s.add(tuple(x))


print("there are ",len(s),"possible permutations")


for x in s:
    for y in x:
        print(y,end=" ")
    print()