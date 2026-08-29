import sys 
d_char = sys.stdin.read()
data = d_char.strip().split("\n")
darr=[]
darruums=[]
for x in data:
    if x.find(" * ")>-1:
        darr.append(x.split())
        darruums.append(x)
    else:
        
        darruums.append(x.split(" "))
        print(x.strip().split(), len(x.strip().split())) 
        darr.append(x.strip().split())

print(darruums)


swapped = list(zip(*darr))
res =0
res2=0
for x in enumerate(swapped):
    vals =  x[1][:-1]
    operator=str(x[1][len(x[1])-1])
    tmp=0
    for v in vals:
        if operator=="*":
            if tmp==0:
                tmp=1
            tmp *=int(v)
        elif operator=="+":
            tmp +=int(v)
    res +=tmp
print(res)
rez=0

data=[]
grid=[]
for x in d_char.split("\n"):
    data=[]
    for char in x:
        data.append(str(char))
    if len(data)>0:
        grid.append(data)
for x in grid:
    print(x)
operator=""
res2=0
tmp_vals=[]
max_len = max(len(row) for row in grid)
gridtransponsed = list(zip(*grid))

def calcimussi(tmp_vals, operator, res):
    tmp=0
    for x in tmp_vals:
        if operator=="*":
            if tmp==0:
                tmp=1
            tmp*=x
        elif operator=="+":
            tmp+=x

    return res+tmp

for x in gridtransponsed:
    print(x)
print(gridtransponsed[len(gridtransponsed)-1])
for x in gridtransponsed:
    print("oneline:", x)
    tmp=0
    if set(x)=={' '}:
        #calc above
        print("new kids on the block",x)
        print("vals:", tmp_vals)
        res2=calcimussi(tmp_vals, operator, res2)
        tmp_vals=[]
        
    else:
        tmp=""
        for v in x:
            if v[len(v)-1]=="*":
                operator = v
                
            elif v[len(v)-1]=="+":
                operator=v
            else:
                tmp+=v
        tmp_vals.append(int(tmp))
        print("tmp_vals", tmp_vals)            

print(calcimussi(tmp_vals, operator, res2))
