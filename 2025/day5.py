from re import A
import sys
data = sys.stdin.readlines()
good=[]
incredients=[]

for r in data:
    if r.find("-")>-1:
        a, b = map(int, r.strip().split("-"))
        good.append((a,b))
    elif r.strip()=='':
        pass
    else:
        incredients.append(int(r.strip()))
    
njam=0
puke=0

for incred in incredients:
    if any(a <= incred <= b for a,b in good):
        njam+=1
    else:
        puke+=1
print("puke:", puke)
print("njam:", njam)

good.sort()
merged = []
for start, end in good:
    if merged and start <= merged[-1][1] + 1:
        merged[-1] = (merged[-1][0], max(merged[-1][1], end))
    else:
        merged.append((start, end))

print(sum(b-a +1 for a,b in merged))
