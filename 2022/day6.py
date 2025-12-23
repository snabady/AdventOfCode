# mjqjpqmgbljsphdztnvjfqwrcgsmlb
import sys 

data = sys.stdin.read()
#data = list(data.strip())
data=data.strip()
done=False
for i,x in enumerate(data.strip()):
    if done:
        break
    if i>14:
         
        substr=data[i-14:i]
        print("substring", substr)
        for iv,xv in enumerate(substr):
            substr = substr.replace(xv,xv.upper(),1)
            if xv in substr:
                break 
            elif iv== len(substr)-1:
                print(data[i-13:i], "starting at index:", i)
                done=True
                break

    
