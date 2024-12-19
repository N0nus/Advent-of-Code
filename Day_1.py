list1 = []
list2 = []

with open('Advent_of_Code/day1input.txt', 'r') as file:
    for i, num in enumerate(file.read().split()):
        if i % 2 == 0:  # Select every other number
            list1.append(int(num))
        else:
            list2.append(int(num))

new_list1 = list1.copy()
new_list2 = list2.copy()

total = 0

for i in range(0,len(list1)):
    smallest1 = 0
    smallest2 = 0
    for j in range(0,len(list1)):
        if(list1[smallest1] >list1[j]):
            smallest1 = j
    for k in range(0,len(list2)):
        if(list2[smallest2] > list2[k]):
            smallest2 = k
    total += abs(list2[smallest2]-list1[smallest1])
    list1.pop(smallest1)
    list2.pop(smallest2)
print(total)

total = 0


for i in range(0,len(new_list1)):
    for j in range(0,len(new_list2)):
        if(new_list1[i] == new_list2[j]):
            total += new_list1[i]
print(f"total = {total}")

            