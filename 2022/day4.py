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

def checkoverlapping(x):
    x1=range(x[0][0],x[0][1])
    x2=range(x[1][0],x[1][1])
    print(x1, x2)
    if x1 in x2:
        print(x1, x2)
    if x2 in x1:
        print(x1, x2)
data = parsedata()
# range(start,stop, step)


for x in data:
    print(x, checkoverlapping(x))
