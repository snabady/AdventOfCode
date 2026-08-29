pw2 =0
pw1 =0
val = 50
with open ("input1.txt") as f:
    for line in f:
        
        command = line[0:1]
        shift_val = int(line[1:].strip())
        for i in range(shift_val):

            if command == "L":
                val = (val-1+100)%100
            else:
                val = (val+1)%100

            if val == 0:
                pw2 += 1
        if val==0:
            pw1+=1

print(pw1)
print(pw2)
