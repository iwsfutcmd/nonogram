from itertools import product
from fractions import Fraction
def row_possibilities(pattern, curr_row):
    row_length = len(curr_row)
    possibilities = []
    tight_row_length = sum(pattern) + len(pattern) - 1
    for offsets in product(range(row_length - tight_row_length + 1), repeat=len(pattern)):
        possibility = [False] * offsets[0] + [True] * pattern[0]
        for length, offset in zip(pattern[1:], offsets[1:]):
            possibility.extend([False] * (offset + 1))
            possibility.extend([True] * length)
        for i in range(row_length - len(possibility)):
            possibility.append(False)
        if len(possibility) != row_length:
            continue
        if all([any([c == p == True, c == p == False, c == None]) for c, p in zip(curr_row, possibility)]):
            possibilities.append(possibility)
    output = []
    for z in zip(*possibilities):
        if all(z):
            output.append(True)
        elif not any(z):
            output.append(False)
        else:
            output.append(None)
    return output
    # return [Fraction(sum(z), len(z)) for z in zip(*possibilities)]

def solve(x, y, curr_puz=None):
    if not curr_puz:
        curr_puz = [[None] * len(y)] * len(x)
    output = [[cell for cell in row] for row in curr_puz]
    for i, (pattern, curr_row) in enumerate(zip(x, output)):
        output[i] = row_possibilities(pattern, curr_row)
    output = [[output[j][i] for j in range(len(output))] for i in range(len(output[0]))] 
    for i, (pattern, curr_row) in enumerate(zip(y, output)):
        output[i] = row_possibilities(pattern, curr_row)
    output = [[output[j][i] for j in range(len(output))] for i in range(len(output[0]))] 
    if all([all([cell != None for cell in row]) for row in output]):
        return output
    else:
        return solve(x, y, output)

def render(puz):
    for row in puz:
        output = []
        for cell in row:
            if cell == True:
                output.append("#")
            elif cell == False:
                output.append(".")
            else:
                output.append("o")
        print(" ".join(output))

def string_to_blocks(string):
    output = []
    for substring in string.split(" "):
        output.append([0 if c == "0" else ord(c.upper()) - 64 for c in substring])
    return output

def nums_to_blocks(nums):
    output = []
    for substring in nums.split("."):
        output.append([int(c) for c in substring.split(",")])
    return output

curr_puz = [[None] * 8] * 9
x = [[3], [2,1], [3,2], [2,2], [6], [1,5], [6], [1], [2]]
y = [[1,2], [3,1], [1,5], [7,1], [5], [3], [4], [3]]