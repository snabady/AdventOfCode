import hashlib

pi= "bgvyzdsv"
#pi ="abcdef"
key=0
while True:
    pin = pi + str(key)
    if hashlib.md5(pin.encode()).hexdigest().startswith("000000"):
        break
    key +=1

print(key)
