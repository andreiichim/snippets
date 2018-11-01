
-- Magnitude of vector v
length v

-- u + v
u + v

-- u - v
u - v

-- v + c
c*v

--  Dot product
dot u v

-- Cross product
cross u v

-- Vector normalization
normalize v

-- Projection of point c on the line between point a and point b
fn pointLineProj pA pB pC =
(
	local vAB = pB-pA
	local vAC = pC-pA
	local d = dot (normalize vAB) (normalize vAC)
	return (pA+(vAB*(d*(length vAC/length vAB))))
)
  
-- Intersection between a line (defined by linePoint and lineVector) and a plane (defined by planePoint and planeNormal)
fn planeLineIntersect planePoint planeNormal linePoint lineVector = 
(
	local lineVector = normalize lineVector
	local d1 = dot (planePoint-linePoint) planeNormal
	local d2 = dot lineVector planeNormal
	if abs(d2) < 0.0000000754 then
	(
		if abs(d1) > 0.0000000754 then return 0
		else return -1
	)
	else
	(
		return linePoint + ( (d1/d2)*lineVector )
	)
)
