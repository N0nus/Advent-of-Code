mul1 = 0
mul2 = 0
total = 0
enabled = True
with open('Advent_of_Code/day3input.txt', 'r') as file:
    content = file.read()
    for i, ch in enumerate(content):
        if content[i:i+3] == "do(":
            enabled = True
        if content[i:i+6] == "don't(":
            enabled = False
        if content[i:i+4] == "mul(":
            if not enabled:
                continue
            j = i+4
            print(content[i:i+12])
            while content[j] != ',':
                j += 1
            try:
                int(content[i+4:j])
                print(content[i+4:j])
                mul1 = content[i+4:j]
            except ValueError:
                continue
            k = j+1
            while content[j] != ')':
                j += 1
            try:
                int(content[k:j])
                print(content[k:j])
                mul2 = content[k:j]
            except ValueError:
                continue
            total += int(mul1)* int(mul2)
print(total)
