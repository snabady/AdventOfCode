# l
# w
# h
# survace = 2 * l * w
#        += 2 * w * h 
#        += 2 * h * l
#        + surface of smallest side

# PART 2
# shortest distance around its sides OR
# perimeter: 2*l + 2*w | 2(l+w)
# PLUS
# cubic feet of volume of the present

with open ("input2.txt") as f:
    result = 0
    ribbon_result=0
    for x in f:
        l, w, h = x.split("x")
        l =int(l)
        w=int(w)
        h=int(h)
        t_smallest_sides = sorted([l,w,h])
        shortest_distance_sides=2*t_smallest_sides[0] + 2*t_smallest_sides[1]
        cubic_feet= h*l*w
        onepackage = 2*l*w + 2*w*h + 2*h*l + t_smallest_sides[0]*t_smallest_sides[1]
        oneribbon = shortest_distance_sides+cubic_feet
        result += onepackage
        ribbon_result+=oneribbon
        print (onepackage)

    print(f"wrapping_paper needed: {result}")

    print(f"ribbon_result needed: {ribbon_result}")
