#*%\@/*%$%*\@/*%$%*%\@/*%$%*\@/*%$%*\@/*%$%\^/*%$%\@/*%$%**\@/*%$%*\@/*%$%*\@/*%$%*\@/*%*
#*  X   !   X   !   X   !   X   !   X   !   .   !   X   !   X   !   X   !   X  !   X  ! *
#*      O       O       O       O       O  .|.  O       O       O       O      O      O *
#*                                         -*-                                          *
#*                                         '|`                                          *
#*                                         *:*                                          *
import sys

data =sys.stdin.readlines()

def getrectsize(x,y):
    xx=abs(x[0]-y[0])+1
    yy=abs(x[1]-y[1])+1
    return xx* yy

din=[]
for l in data:
    din.append([int(x) for x in  l.split(",")])
max_rect=0
for i in range(len(din)):
    for j in range(i+1, len(din)):
        current_rect = getrectsize(din[i], din[j])
        if current_rect> max_rect:
            max_rect=current_rect
#din.sort(key=lambda x:x[0])
print(din)
print(max_rect)
