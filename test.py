import random

print()
nums = []

for num in range(20):
    nums.append(random.randint(1, 500)); sep=''

max = nums[0]
for i in nums:
    if i > max:
        max = i

print(nums)
print("The maximum value that appears in the list is " + str(max) + ".")

#this line will print index of MAXIMUM value
print("index of maximum value is :",nums.index(max))