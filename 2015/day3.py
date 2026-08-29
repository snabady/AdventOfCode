# MOVES
# starting point +1
# ^ - 1 North
# v - 1 South
# < - 1 West
# > - 1 East
# end point +1
# 
# [][]

from collections import defaultdict
x = 0
y = 0
xr =0
yr =0


def move (x, y, char):
    if char == ">":
        x += 1
    elif char == "<":
        x -= 1
    elif char == "^":
        y+=1
    elif char=="v":
        y-=1
    else:
        print("invalid char")
    return x, y

with open ("input3.txt") as f:
    houses = defaultdict(int)
    x=0
    y=0
    for xx in f:
        for i,char in enumerate(xx):
            if i%2==0 :
                x, y =move(x,y, char)
                houses[(x,y)] += 1
            else:
                xr,yr = move (xr,yr, char)
                houses[(xr, yr)] +=1

        houses[(x,y)] += 1
        houses[(xr,yr)]+=1
    print( len(houses))
