array = []
with open('Advent_of_Code/day4input.txt', 'r') as file:
    content = file.read()
    array = content.splitlines()

DIRECTIONS = [
    (0, 1),    # Right
    (0, -1),   # Left
    (1, 0),    # Down
    (-1, 0),   # Up
    (1, 1),    # Diagonal down-right
    (1, -1),   # Diagonal down-left
    (-1, 1),   # Diagonal up-right
    (-1, -1)   # Diagonal up-left
]

word_string = "XMAS"
word_length = len(word_string)
total = 0

for i, row in enumerate(array):
    for j in range(len(row)):
        if array[i][j] == word_string[0]:  # Start matching only if the first character matches
            for direction in DIRECTIONS:
                found = True
                for k in range(word_length):
                    ni = i + k * direction[0]
                    nj = j + k * direction[1]
                    
                    # Boundary check
                    if ni < 0 or ni >= len(array) or nj < 0 or nj >= len(row):
                        found = False
                        break
                    
                    if array[ni][nj] != word_string[k]:
                        found = False
                        break
                
                if found:
                    total += 1
                    print(f"Found '{word_string}' starting at ({i}, {j}) in direction {direction}")

print(f"Total occurrences: {total}")
