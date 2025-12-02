import re
with open ("input8.txt") as f:
    str_cnt =0
    str_cnt_esc = 0
    for i, line in enumerate(f):
        
        line= line.strip()
        str_cnt += len(line)
        line = line[1:-1]
        escapes = [ r'\\\\', r'\\"' , r"\\x[0-9A-Fa-f]{2}"]
        for i,x in enumerate(escapes):
            line = re.sub(x, ".",line )
        str_cnt_esc += len(line)
    print(str_cnt, str_cnt_esc)
        
    print(f"reslut: {str_cnt - str_cnt_esc}")


