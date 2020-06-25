def equilateral(sides):
    return congruity(sides) == 1

def isosceles(sides):
    return congruity(sides) in (1,2)

def scalene(sides):
    return congruity(sides) == 3

# Helper
def congruity(sides:list):
    sides.sort()
    side_set = set(sides)
    is_valid = sides[0] + sides[1] > sides[2]
    if len(side_set) in (1,2,3) and is_valid:
        return len(side_set)
    else:
        return 0
