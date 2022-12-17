def belongsToLine(coord):
    ans = {(i,j): (i**2 + j**2)**(1/2) for i,j in coord if j == 5*i - 2}
    return ans