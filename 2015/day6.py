rows=1000
cols=1000
matrix = [[ False for _ in range(cols)] for _ in range(rows)]

brightness = [[ 0 for _ in range(cols)] for _ in range(rows)]
instructions =open("input6.txt").readlines()

def parse_coordinates(vals, position, ret_position):
    return int(vals[position].split(",")[ret_position])

for instruct in instructions:
    # turn on 489,959 through 759,964
    startx=0 
    starty=0 
    endx=0 
    endy=0
    vals = instruct.split(" ")
    if instruct.startswith("turn on") or instruct.startswith("turn off"):
        startx = parse_coordinates(vals,2,0)
        starty = parse_coordinates(vals,2,1)
        endx =parse_coordinates(vals,4,0)
        endy =parse_coordinates(vals,4,1)
    elif instruct.startswith("toggle"):
        startx = parse_coordinates(vals,1,0)
        starty = parse_coordinates(vals,1,1)
        endx =parse_coordinates(vals,3,0)
        endy =parse_coordinates(vals,3,1)

    for i in range (startx, endx+1):
        for j in range (starty, endy+1):
            if instruct.startswith("turn on"):
                matrix[i][j]=True
                brightness[i][j]+=1
            elif instruct.startswith("turn off"):
                matrix[i][j]=False
                if brightness[i][j]>0:
                    brightness[i][j]-=1
            elif instruct.startswith("toggle"):
                brightness[i][j]+=2
                matrix[i][j]= not(matrix[i][j])

count = 0
for row in matrix:
    for val in row:
        if val:
            count += 1

print(count)
bright_count =0
for row in brightness:
    for val in row:
        bright_count +=val
print(bright_count)
