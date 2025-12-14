import sys 

def parsedata()-> list[list[str]]:

    ret = []
    ret2=[]
    x = sys.stdin.readlines()
    for xval in x:
        xval=xval.strip()
        x1= xval[0:int(len(xval)/2)]
        x2 =xval[int(len(xval)/2):]
        #print("len(str):", len(xval), "len(parts):",len(x1), len(x2))
        ret.append([x1,x2])
    cnt=3
    group =[]
    for xval in x:
        xval =xval.strip()
        if cnt>0:
            group.append(xval)
            cnt-=1
        if cnt ==0:
            ret2.append(group)
            group=[]
            cnt=3
    return ret,ret2

def get_prio_points(ch):
    if ord(ch)>96:
        return (ord(ch)-96)
    else:
        return (ord(ch)-38)

data,data2 = parsedata()
res1=0
for x,y in data:
    for ch in x:
        if ch in y:
            res1+=get_prio_points(ch)
            break
print("part1:", res1)

res2=0
for x in data2: 
#    print(x[0], x[1], x[2])
    for char in x[0]:
        if char in x[1] and char in x[2]:
            res2+=get_prio_points(char)
            break
print("part2:", res2)
