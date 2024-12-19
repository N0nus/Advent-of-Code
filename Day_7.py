import itertools

def validate(sum, nums):

    operations = ["+", "*", "|"]

    repeat = (len(nums)-1)
    combos = itertools.product(operations, repeat=repeat)

    for combo in combos:
        total = nums[0]
        for i in range(len(nums)-1):
            if combo[i] == "*":
                total *= nums[i+1]
            elif combo[i] == "+":
                total += nums[i+1]
            elif combo[i] == "|":
                total = int(str(total) + str(nums[i+1]))
            

            if total > sum:
                break
        if total == sum:
            return 1
    return 0






sums = []
nums_list = []

with open('Advent_of_Code/day7input.txt') as file:
    for line in file:
        line = line.strip()
        sums.append(int(line.split(":")[0]))
        nums_list.append(list(map(int, line.split(":")[1].split())))



total_sum = 0
for i in range(len(sums)):
    if validate(sums[i], nums_list[i]) == 1:
        total_sum += sums[i]

print(total_sum)
