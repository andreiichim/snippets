
import math

# Magnitude of vector v
def magnitude(v):
    return math.sqrt(sum(v[i]*v[i] for i in range(len(v))))

# u + v
def add(u, v):
    return [ u[i]+v[i] for i in range(len(u)) ]

# u - v
def sub(u, v):
    return [ u[i]-v[i] for i in range(len(u)) ]

# v * constant c
def mul(v, c):
    return [ i*c for i in v ]

# Dot product of u and v
def dot(u, v):
    return sum( u[i]*v[i] for i in range(len(u)) )

# Normalize vector v
def normalize(v):
    vmag = magnitude(v)
    return [ v[i]/vmag  for i in range(len(v)) ]

# Distance between point a and point b
def distance(a, b):
    return math.sqrt ( sum( [ a[i]-b[i])**2 for i in range(len(a)) ] ) )

# Projection of point c on the line between point a and point b
def point_line_projection(a, b, c):
    ba = sub(b, a)
    ca = sub(c, a)
    d = dot(normalize(ba), normalize(ca))
    return magnitude( add( a,( mul( ba,( d*(magnitude(ca)/magnitude(ba)) ) ) ) ) )

# Intersection between a line (defined by linePoint and lineVector) and a plane (defined by planePoint and planeNormal)
def plane_line_intersect(planePoint, planeNormal, linePoint, lineVector):
    lineVector = normalize(lineVector)
    d1 = dot(sub(planePoint, linePoint), planeNormal)
    d2 = dot(lineVector, planeNormal)
    if abs(d2) < 0.0000000754:
        if abs(d1)> 0.0000000754:
            return 0
        else:
            return -1
    else:
        return add(linePoint, [v*(d1/d2) for v in lineVector])
