# Snippets

## Geometry
Input parameters:
  - points: pA, pB, pC, pD
  - vectors:
    - vAB = pB-pA
  - lines: defined by two points: AB
  - planes:
    - defined by three points: ABC
    - defined by one point and two vectors: pP, vAB, vAC
    - defined by a point and a normal: pA, pN
    
### Magnitude
Returns the lenght of the vector.

### Add
Returns the sum of two vectors.

### Sub
Returns the sum between a vector and the second vector reversed.

### Mul
Returns a vector with the same direction but lenght * scalar.

### Dot Product
Returns a scalar.
When two vectors are at right angles the dot product is 0.

### Cross Product
Returns a vector that is perpendicular to both vectors.
When two vectors point in the same direction the cross product is 0.

### Normalize
Returns a vector pointing in the same direction but of lenght 1.

### Distance
Returns the distance between two points.
