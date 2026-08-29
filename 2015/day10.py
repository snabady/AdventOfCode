d_input="1321131112"
expected="11131221133112"

for i in range(40):
    print(i)
    prev =d_input[0]
    cnt =1

    output =""
    for x in d_input[1:]:
        if x ==prev:
            cnt +=1
        elif x!= prev:

            output+=str(cnt)+str(prev)
            cnt =1
            prev =x
    output += str(cnt) + prev
    d_input = output
print(d_input)
print(len(d_input))

def look_and_see(s: str) -> str:
    parts = []
    prev = s[0]
    cnt = 1

    for x in s[1:]:
        if x == prev:
            cnt += 1
        else:
            parts.append(str(cnt))
            parts.append(prev)
            prev = x
            cnt = 1

    parts.append(str(cnt))
    parts.append(prev)
    return "".join(parts)


d_input = "1321131112"
for _ in range(50):
    d_input = look_and_see(d_input)

print(len(d_input))
