import sys

def has_two_idents(value):
    s = str(value)
    length = len(s)

    if length % 2 != 0:
        return False

    half = length // 2
    first_half = s[:half]
    second_half = s[half:]

    if first_half == second_half:
        return True
    else:
        return False
def is_repeated_pattern(value):
    s = str(value)
    n = len(s)

    for num_blocks in range(2, n + 1):
        if n % num_blocks == 0:
            block_size = n // num_blocks
            block = s[:block_size]

            is_valid = True
            for i in range(0, n, block_size):
                if s[i:i + block_size] != block:
                    is_valid = False
                    break

            if is_valid:
                return True

    return False
D = sys.stdin.read()
res1=0
res2=0
ranges = D.split(",")
for r in ranges:
    first,last = r.split("-")
    for x in range(int(first),int(last)+1):
       
        if has_two_idents(x):
            res1+=x
        if is_repeated_pattern(x):
            res2+=x
print (res1)
print(res2)
