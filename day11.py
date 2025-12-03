p_in="hepxcrrq"
example=["hijklmmn","abbceffg","abbcegjk"] # 0=false,1=false, 2=false
next_pws = [{"abcdefgh":"abcdffaa"},{"ghijklmn":"ghjaabcc"}]
#hae
# jo ... erst ma pennen wa 
not_allowed_chars=["i","o","l"]

def check_three_letter_rule(pwd):
    threesomes =[]
    pwd = str(pwd)
    i=0
    for _ in pwd:
        if i+3 <= len(pwd)  :
            threesomes.append(pwd[i:i+3])
        i+=1
    good_threesomes=[]
    
    for pair in threesomes:
        three=1
        for i,x in enumerate(pair):
            if i+1 <len(pair):
                if ord(x)+1 == ord(pair[i+1]):
                    three += 1
            if three ==3:
                good_threesomes.append(pair)
                return True
    return False
def has_no_forbidden(pwd):
    for x in not_allowed_chars:
        if x in pwd:
            return False
    return True
def has_double(pwd):
    pairs=set()
    i=0
    while i<len(pwd)-1:
        if pwd[i]==pwd[i+1]:
            pairs.add(pwd[i])
            i+=2
        else:
            i+=1
    return len(pairs)>=2

def check_rulez(pwd):
    return has_double(pwd) and has_no_forbidden(pwd) and check_three_letter_rule(pwd)

def get_next_password(pwd):
    pwd = list(pwd)
    i = len(pwd)-1
    while i>0:
        if pwd[i]=='z':
            pwd[i]='a'
            i-=1
        else:
            pwd[i] =chr(ord(pwd[i])+1)
            break
    return "".join(pwd)

def get_valid_password(pwd):
    pwd = get_next_password(pwd)
    while not check_rulez(pwd):
        pwd = get_next_password(pwd)
    return pwd

for x in example:
    print(x, check_rulez(x))
    print("--------------")
puzzle = "abcdefgh"
puzzle="abcdefgh"
print(get_valid_password(puzzle))
puzzle="ghijklmn"
print(get_valid_password(puzzle))
puzzle="hepxcrrq"
print(get_valid_password(puzzle))
puzzle="hepxxyzz"
print(get_valid_password(puzzle))

