import copy
import sys 
from dataclasses import dataclass


@dataclass 
class Move():
    steps: int 
    startpile: int
    endpile: int

def parsedata():
    data = sys.stdin.readlines()
    stackpiles=[] 
    stacks=[]
    moves=[]
    rdytomove=False
    for x in data:
        if not rdytomove:
            if x.replace("\n","")=="":
                rdytomove=True
            else:
                stackpiles.append(x.replace("\n",""))
                print("asdf",x.replace("\n",""))
        else:
            x = x.strip().split(" ")
            moves.append(Move(steps=int(x[1]),
                              startpile=int(x[3]),
                              endpile=int(x[5]))
                         )

    cols =[]
    for i in range(len(stackpiles)):
        x=stackpiles.pop()
        if i==0:
            for xi, xv in enumerate(x):
                if xv!=" ":
                    cols.append(xi)
            print("col#:", cols)
        elif i==1:
            for id in cols:
                pile =[]
                pile.append(x[id])
                stacks.append(pile)
        else:
            for i,stack in enumerate(stacks):
                if x[cols[i]]!=" ":
                    stack.append(x[cols[i]])

    print("stacks:", stacks)
    return stacks, moves

# stack lifo -> append/pop... done
stacks, moves = parsedata()
stack2=copy.deepcopy(stacks)
for x in moves:
    for i in range(x.steps):
        stacks[x.endpile-1].append(stacks[x.startpile-1].pop())

res=""
for piles in stacks:
    res += piles.pop()
print("res1", res)
for x in moves:
    for i in range(x.steps):
        stack2[x.endpile-1].insert(len(stack2[x.endpile-1])-i, stack2[x.startpile-1].pop())
res2=""
for x in stack2:
    res2+= x.pop()

print("res2:", res2)
