def farthestPoint(coord):
    ans = [(i**2 + j**2)**(1/2) for i,j in coord if i > 0 and j > 0]
    return max(ans)