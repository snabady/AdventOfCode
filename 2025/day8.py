import math


def distance(a, b):
    dx = a[0] - b[0]
    dy = a[1] - b[1]
    dz = a[2] - b[2]
    return math.sqrt(dx * dx + dy * dy + dz * dz)


filename = "input8.txt"
num_connections = 1000

with open(filename, "r", encoding="utf-8") as f:
    input_lines = f.readlines()

locations = []

for line in input_lines:
    x, y, z = map(int, line.strip().split(","))
    locations.append((x, y, z))

distances = []

for i in range(len(locations)):
    for j in range(i + 1, len(locations)):
        a = locations[i]
        b = locations[j]
        d = distance(a, b)
        distances.append((a, b, d))

distances.sort(key=lambda x: x[2])

circuits = []

part1 = 0
part2 = 0

for i in range(len(distances)):

    a, b, d = distances[i]

    if i == num_connections:
        circuits.sort(key=len, reverse=True)
        part1 = len(circuits[0]) * len(circuits[1]) * len(circuits[2])

    circuit_contains_a = -1
    circuit_contains_b = -1

    for idx in range(len(circuits)):
        if a in circuits[idx]:
            circuit_contains_a = idx
        if b in circuits[idx]:
            circuit_contains_b = idx

    if circuit_contains_a == circuit_contains_b:

        if circuit_contains_a == -1:
            circuits.append([a, b])

    elif circuit_contains_a == -1:
        circuits[circuit_contains_b].append(a)

    elif circuit_contains_b == -1:
        circuits[circuit_contains_a].append(b)

    else:
        circuits[circuit_contains_a].extend(
            circuits[circuit_contains_b]
        )
        del circuits[circuit_contains_b]

    if len(circuits[0]) == len(locations):
        part2 = a[0] * b[0]
        break

print(filename, ": part1 =", part1, ", part2 =", part2)

