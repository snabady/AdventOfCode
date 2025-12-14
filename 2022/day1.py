import sys
from dataclasses import dataclass 

@dataclass
class Elves():
    calories: list[int]
    ident: int

    @property 
    def total_cal(self)-> int:
        return sum(self.calories)

data = sys.stdin.readlines()

elves: list[Elves]= []
cals: list[int] = []
for i, cal in enumerate(data):
    cal =cal.strip()
    if cal =="":
        elves.append(Elves( calories=cals, ident=len(elves)+1))
        cals =[]
    else:
        cals.append(int(cal)) 

#
#max_cal_elve=0
#best_elve=None
#for elve in elves:
#    if elve.total_cal>=max_cal_elve:
#        max_cal_elve = elve.total_cal
#        best_elve= elve
#
#print(best_elve, best_elve.total_cal)
best_elve = max(elves, key=lambda e: e.total_cal)
elves.sort( key=lambda e: e.total_cal, reverse=True)
top_3=elves[:3]
p2sum= sum( cal.total_cal for cal  in top_3)

print(best_elve, best_elve.total_cal)
print(p2sum)
