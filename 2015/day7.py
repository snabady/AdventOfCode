wires={}
instruction ={}
with open("input7.txt") as f:
    for line in f:
        cmd, wire = line.strip().split(" -> ")
        instruction[wire] = cmd.strip()

def get_value(wire):
    if wire.isdigit():
        return int(wire)
    if wire in wires:
        return wires[wire]

    cmd = instruction[wire]

    if "AND" in cmd:
        a, b = cmd.split(" AND ")
        val = get_value(a) & get_value(b)
    elif "OR" in cmd:
        a, b = cmd.split(" OR ")
        val = get_value(a) | get_value(b)
    elif "LSHIFT" in cmd:
        a, s = cmd.split(" LSHIFT ")
        val = get_value(a) << int(s)
    elif "RSHIFT" in cmd:
        a, s = cmd.split(" RSHIFT ")
        val = get_value(a) >> int(s)
    elif "NOT" in cmd:
        v = cmd.split("NOT ")[1].strip()
        val = ~get_value(v) & 0xffff
    else:
        val = get_value(cmd)

    wires[wire] = val
    return val
print(get_value("a"))
wires ={}
wires["b"]=956
print(get_value("a"))
