# ( +1
# ) -1

with open("/home/sna/src/adventofcode/2015/input1.txt") as f:
    lines =0
    result = 0
    basement=False
    first_time_basement_floor=None
    for i,x in enumerate(f.readline()):
        lines+=1
        if x =="(":
            result += 1
        elif x==")":
            result -= 1

        if result == -1 and not basement:
            first_time_basement_floor = i+1
            basement = True 
            print (f"first_time_basement_floor: {first_time_basement_floor}")
    print (f"lines: {lines}")
    print (f"result: {result}")
    print (f"first_time_basement_floor: {first_time_basement_floor}")
