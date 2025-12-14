import sys

def parsedata():
    data =sys.stdin.readlines()
    ret=[]
    for x in data:
        parta,partb=x.strip().split(",")
        paira = [int(x) for x in parta.split("-")]
        pairb=[int(x) for x in partb.split("-")]
        ret.append((paira,pairb))
    return ret

def checkoverlapping(x, whole=False, some=False):
    x1, x2 = x[0][0],x[0][1]
    y1, y2 = x[1][0],x[1][1]
    if whole:
        if x1 in range(y1,y2+1) and x2 in range(y1,y2+1):
        #    print(x1,x2 , "in", range(y1,y2+1))
            return True
        elif y1 in range(x1,x2+1) and y2 in range(x1,x2+1):
         #   print(y1,y2 in range(x1,x2+1))
            return True
    if some:
        if x1 in range(y1,y2+1) or x2 in range(y1,y2+1) or y1 in range(x1, x2+1) or y2 in range(x1,x2+1):
            return True
    return False

data = parsedata()
# range(start,stop, step)

part1=0
part2=0
for x in data:
    #print("-->",x)
    if checkoverlapping(x, whole=True):
        part1+=1
    if checkoverlapping(x, some=True):
        part2+=1

print("part1: ", part1)
print("part2: ", part2)
