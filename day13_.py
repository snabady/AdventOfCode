import sys 
import itertools
puzzle = sys.stdin.readlines()
attendees=[]
attendees_love={}
for line in puzzle:
    line = line.strip()
    line = line.replace("would ", "")
    line=line.replace(" happiness units by sitting next to","")
    line =line.replace(".","")
    parts = line.split(" " )
    if parts[1]=="gain":
        happiness=int(parts[2])
    else:
        happiness=int(parts[2])*-1
    attendees_love[(parts[0]),(parts[len(parts)-1])]=happiness
    attendees.append(parts[0])
    attendees.append(parts[3])
attendees = list(set(attendees))
attendees.append("ICH")
print(attendees)
possible_seats=list(itertools.permutations(attendees))
print(len(possible_seats), "possible permutations")

groupiness=[]
for j,seats in enumerate(possible_seats):
    tmp=0
    for i,seat in enumerate(seats):
        if i==len(seats)-1:
            partners=seats[i],seats[0]
            p2 =seats[0],seats[i]
        else:
            partners = seats[i], seats[i+1]
            p2 =seats[i+1],seats[i]
        if(partners in attendees_love):
            tmp += attendees_love[partners]
            tmp+=attendees_love[p2]
        else:
            break

    groupiness.append(tmp)


print("worst case\t", min(groupiness))
print("best_case\t", max(groupiness))
