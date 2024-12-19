def is_valid(update, rules):
    for rule in rules:
        if rule[0] in update and rule[1] in update:
            if update.index(rule[0]) > update.index(rule[1]):
                return False
    return True

def reorder(update, rules):
    while not is_valid(update, rules):
        for rule in rules:
            if rule[0] in update and rule[1] in update:
                if update.index(rule[0]) > update.index(rule[1]):
                    update[update.index(rule[0])], update[update.index(rule[1])] = update[update.index(rule[1])], update[update.index(rule[0])]
    return update

x = 0
rules = []
updates = []
ruling = True
with open('Advent_of_Code/day5input.txt', 'r') as file:
    content = file.read()
    for line in content.splitlines():
        if ruling:
            try:
                rules.append(tuple(map(int, line.split("|"))))
            except ValueError:
                ruling = False
        elif not ruling:
            updates.append(list(map(int, line.split(","))))


index_1 = 0
index_2 = 0
valid_updates = []
valid = True
invalid_updates = []

for update in updates:
    valid = is_valid(update, rules)
    if valid:
        valid_updates.append(update)
    else:
        invalid_updates.append(reorder(update, rules))

total = 0
for update in valid_updates:
    total += update[(len(update)//2)]
print(total)

second_total = 0
for update in invalid_updates:
    second_total += update[(len(update)//2)]
print(second_total)
                
                

