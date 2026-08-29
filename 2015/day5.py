import re

with open ("input4.txt") as f:
    nice_strings = 0
    for line in f:
        req_vowels = False
        req_double_letter= False
        req_forbidden_str=False
        vowels =  ["a","e","i","o","u"]
        forbidden_str=["ab", "cd", "pq", "xy"]
        p_char =""
        vowel_cnt =0
        for i, char in enumerate(line):
            if not req_double_letter and char == p_char:
                req_double_letter=True
            if char in vowels:
                vowel_cnt+=1
            if not req_forbidden_str and (p_char+char) in forbidden_str:
                req_forbidden_str = True
                break
            p_char = char
            

        if vowel_cnt >= 3  and req_double_letter and not req_forbidden_str:
            
            nice_strings+=1
    print(f"nice strings: {nice_strings}")


pair_regex = r"(([a-z][a-z]).*\2)"
letter_regex = r"(([a-z]).\2)"
nice =0
with open ("input4.txt") as f:
    for line in f:
        if re.search(pair_regex, line) and re.search(letter_regex, line):
            nice +=1
    print(f"nice: {nice}")
