import sys
puzzle = sys.stdin.read()
res1=0
res2=0

def best_digits(line,bestlen):
    stack = []
    to_remove = len(line) - bestlen
    for digit in line:
        while stack and to_remove > 0 and stack[-1] < digit:
            stack.pop()
            to_remove -= 1
        stack.append(digit)

    return ''.join(stack[:bestlen])

def total_joltage(lines):
    total = 0
    total1=0
    for line in lines.splitlines():
        total += int(best_digits(line.strip(), 12))
        total1 += int(best_digits(line.strip(), 2))
    return total, total1

for line in puzzle.splitlines():
    index_max = max(range(len(line)-1), key=line.__getitem__) 
    rest_line=line[index_max+1:]
    index_two = max(range(len(rest_line)),key=rest_line.__getitem__)
    jolt=f"{line[index_max]}{rest_line[index_two]}"
    res1+=int(jolt)

print(f"puzzle1: {res1}")

print(total_joltage(puzzle))    
