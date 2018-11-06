
import math

# Magnitude of vector vAB
def magnitude(vAB):
    return math.sqrt(sum(vAB[i]*vAB[i] for i in range(len(vAB))))

# vAB + vCD
def add(vAB, vCD):
    return [ vAB[i]+vCD[i] for i in range(len(vAB)) ]

# vAB - vCD
def sub(vAB, vCD):
    return [ vAB[i]-vCD[i] for i in range(len(vAB)) ]

# vAB * constant c
def mul(vAB, c):
    return [ i*c for i in vAB ]

# Dot product of vector vAB and vector vCD
def dot(vAB, vCD):
    return sum( vAB[i]*vCD[i] for i in range(len(vAB)) )

# Cross product of vector vAB and vector vCD
def cross(vAB, vCD):
    r = []
    for i in range(len(vAB)):
        if i == 0:
            j,k = 1,2
            r.append(vAB[j]*vCD[k] - vAB[k]*vCD[j])
        elif i == 1:
            j,k = 2,0
            r.append(vAB[j]*vCD[k] - vAB[k]*vCD[j])
        else:
            j,k = 0,1
            r.append(vAB[j]*vCD[k] - vAB[k]*vCD[j])
    return r

# Normalize vector vAB
def normalize(vAB):
    vmag = magnitude(vAB)
    return [ vAB[i]/vmag  for i in range(len(vAB)) ]

# Normal of a plane defined by three points pA, pB, pC
def plane_normal(pA, pB, pC):
    return normalize( cross( sub(pB,pA), sub(pC,pA) ) )

# Distance between point pA and point pB
def distance(pA, pB):
    return math.sqrt ( sum( [ (pA[i]-pB[i])**2 for i in range(len(pA)) ] ) )

# Point at along% (0-1) between points pA and pB
def alongPoint(pA, pB, along):
    return add( pA, ( mul(sub(pB, pA), along) ) )

# Projection of point pC on the line between point pA and point pB
def point_line_projection(pA, pB, pC):
    vAB = sub(pB, pA)
    vAC = sub(pC, pA)
    d = dot(normalize(vAB), normalize(vAC))
    return add( pA,( mul( vAB,( d*(magnitude(vAC)/magnitude(vAB)) ) ) ) )

# Distance between point pC and the line between point pA and point pB
def point_line_distance(pA, pB, pC):
    return distance(pC, (point_line_projection(pA, pB, pC)) )

# Check if point pC is on the line between point pA and point pB with tolerance
def is_point_on_line(pA, pB, pC, tolerance):
    return (point_line_distance(pA, pB, pC) <= tolerance)

# Intersection between a line (defined by point pA and vector vAB) and a plane (defined by point pP and normal pN)
def plane_line_intersect(pP, pN, pA, vAB):
    vAB = normalize(vAB)
    d1 = dot(sub(pP, pA), pN)
    d2 = dot(vAB, pN)
    if abs(d2) < 0.0000000754:
        if abs(d1) > 0.0000000754:
            return 0
        else:
            return -1
    else:
        return add(pA, [v*(d1/d2) for v in vAB])

def unit_test():
    print ('magnitude([1,2,3]): ', magnitude([1,2,3]))
    print ('add([1,2,3], [4,5,6]): ', add([1,2,3], [4,5,6]))
    print ('sub([1,2,3], [4,5,6]): ', sub([1,2,3], [4,5,6]))
    print ('mul([1,2,3], 0.5): ', mul([1,2,3], 0.5))
    print ('dot([1,2,3], [4,5,6]): ', dot([1,2,3], [4,5,6]))
    print ('cross([1,2,3], [4,5,6]): ', cross([1,2,3], [4,5,6]))
    print ('normalize([1,2,3]): ', normalize([1,2,3]))
    print ('plane_normal([1,2,3], [4,5,6], [1,5,3]): ', plane_normal([1,2,3], [4,5,6], [1,5,3]))
    print ('distance([1,2,3], [4,5,6]): ', distance([1,2,3], [4,5,6]))
    print ('alongPoint([1,2,3], [4,5,6], 0.5): ', alongPoint([1,2,3], [4,5,6], 0.5))
    print ('point_line_projection([1,2,3], [4,5,6], [1,5,3]): ', point_line_projection([1,2,3], [4,5,6], [1,5,3]))
    print ('point_line_distance([1,2,3], [4,5,6], [1,5,3]): ', point_line_distance([1,2,3], [4,5,6], [1,5,3]))
    print ('is_point_on_line([1,2,3], [4,5,6], [7,8,9]): ', is_point_on_line([1,2,3], [4,5,6], [7,8,9], 0.1))
    print ('is_point_on_line([1,2,3], [4,5,6], [1,5,3]): ', is_point_on_line([1,2,3], [4,5,6], [1,5,3], 0.1))
    print ('plane_line_intersect([1,2,3], [1,0,0], [1,2,3], [4,5,6]): ', plane_line_intersect([1,2,3], [1,0,0], [1,2,3], [4,5,6]))

if __name__ == '__main__':
    unit_test()