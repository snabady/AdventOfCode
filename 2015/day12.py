import json 
import re
import sys

puzzle = sys.stdin.read()

res=0
nums = re.findall(r"-?\d+", puzzle)
for x in nums:
    res+=int(x)
print("part1", res)

def sum_non_reds(s):
    if isinstance(s, int):
        return s
    elif isinstance(s, list):
        return sum(sum_non_reds(i) for i in s)
    elif isinstance(s, dict):
        if "red" in s.values():
            return 0
        else:
            return sum(sum_non_reds(i) for i in s.values())

    return 0
with open ("input12.txt") as puzzle:
    print("part1", res)
    print(sum_non_reds(json.load(puzzle)))
