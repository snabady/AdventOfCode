import sys 
from enum import IntEnum

class Game(IntEnum):
    scissor=3
    paper=2
    rock=1

class GameResult(IntEnum):
    draw=0
    lose=2
    win=1
# a-> the players result
def get_round_result( a: Game, b: Game):
    diff = (a-b)%3 
    if diff==0:
        return a+3
    if diff==1:
        return a+6
    return a
   
# b=diff=1-3
def calcMove(a, b):
    a=(a-1)%3
    if b == GameResult.draw:
        b_=a
    elif b == GameResult.win:
        b_=(a+1)%3
    elif b == GameResult.lose:
        b_=(a-1)%3
    return b_+1+gamepoints[b]

playerA={
        'A':Game.rock,
        'B':Game.paper,
        'C':Game.scissor
    }

playerB={
        'X':Game.rock,
        'Y':Game.paper,
        'Z':Game.scissor
    }

gamepoints={
        GameResult.lose: 0, 
        GameResult.draw: 3, 
        GameResult.win: 6,
        }

part2_out={
        "X": GameResult.lose,
        "Y": GameResult.draw,
        "Z": GameResult.win
        }

def parsedata() -> list[list[str]]:
    data = sys.stdin.readlines()
    rounds=[]
    for x in data:
        rounds.append(x.strip().split(" "))
    return rounds

rounds = parsedata()
playerB_points=0
part2=0
for (a_char,b_char) in rounds:
    
    a = playerA[a_char]
    b = playerB[b_char]
    #print("part1:", a_char,b_char,"|", a, b)
    #print("part2:", a_char,b_char,"|", a, part2_out[b_char])
    tmp2= calcMove(a,part2_out[b_char])
    part2+=tmp2
    rnd_r = get_round_result(b,a)
    playerB_points+=rnd_r

print("part1", playerB_points)
print("part2", part2)
