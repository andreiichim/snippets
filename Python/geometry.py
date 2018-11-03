
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

# Plane normal
def plane_normal():
    return normalize (cross(vAB, vAC))

# Distance between point pA and point pB
def distance(pA, pB):
    return math.sqrt ( sum( [ pA[i]-pB[i])**2 for i in range(len(pA)) ] ) )

# Point at along% (0-1) between points pA and pB
def alongPoint(pA, pB, along):
    return add( pA, ( mul(sub(pB, pA), along) ) )

# Projection of point pC on the line between point pA and point pB
def point_line_projection(pA, pB, pC):
    vAB = sub(pB, pA)
    vAC = sub(pC, pA)
    d = dot(normalize(vAB), normalize(vAC))
    return magnitude( add( pA,( mul( vAB,( d*(magnitude(vAC)/magnitude(vAB)) ) ) ) ) )

# Distance between point pC and the line between point pA and point pB
def point_line_distance(pA, pB, pC):
    return distance(pC, (pointLineProj(pA, pB, pC)) )

def is_point_on_line(pA, pB, pC, tolerance):
    return (point_line_distance(pA, pB, pC) <= tolerance)

# Intersection between a line (defined by point pA and vector vAB) and a plane (defined by point pP and normal pN)
def plane_line_intersect(pP, pN, pA, vAB):
    vAB = normalize(vAB)
    d1 = dot(sub(pP, pA), pN)
    d2 = dot(vAB, pN)
    if abs(d2) < 0.0000000754:
        if abs(d1)> 0.0000000754:
            return 0
        else:
            return -1
    else:
        return add(pA, [v*(d1/d2) for v in vAB])
