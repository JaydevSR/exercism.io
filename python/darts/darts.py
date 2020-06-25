def score(x, y):
    in_cir = 1
    mid_cir = 5
    out_cir = 10
    dist = distance((0,0), (x,y))
    if dist <= in_cir:
        return 10
    elif dist <= mid_cir:
        return 5
    elif dist <= out_cir:
        return 1
    else:
        return 0

# Helper
def distance(p1, p2):
    return ((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)**0.5