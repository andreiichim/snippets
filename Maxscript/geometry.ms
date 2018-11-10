
-- Normal of a plane defined by three points pA, pB, pC
fn plane_normal pA pB pC=
    return normalize( cross (pB-pA) (pC-pA) )

-- Point at along% (0-1) between points pA and pB
fn alongPoint pA pB along=
    return pA+(pB-pA)*along

-- Projection of point pC on the line between point pA and point pB
fn point_line_projection pA pB pC =
(
    local vAB = pB-pA
    local vAC = pC-pA
    local d = dot (normalize vAB) (normalize vAC)
    return (pA+(vAB*(d*(length vAC/length vAB))))
)

-- Distance between point pC and the line between point pA and point pB
fn point_line_distance pA pB pC=
    return distance pC (point_line_projection pA pB pC)

-- Check if point pC is on the line between point pA and point pB with tolerance
fn is_point_on_line pA pB pC tolerance=
    return ((point_line_distance pA pB pC) <= tolerance)

-- Intersection between two lines defined by a point (pA, pB) and a vector (a, b)
fn line_line_intersect pA a pB b=
(
    local c = pB - pA
    local cross1 = cross a b
    local cross2 = cross c b
    return pA + a * (dot cross2 cross1) / pow (length(cross1)) 2
)
-- Intersection between a line (defined by point pA and vector vAB) and a plane (defined by point pP and normal pN)
fn plane_line_intersect pP pN pA vAB =
(
    local vAB = normalize vAB
    local d1 = dot (pP-pA) pN
    local d2 = dot vAB pN
    if abs(d2) < 0.0000000754 then
    (
        if abs(d1) > 0.0000000754 then return 0
        else return -1
    )
    else
    (
        return pA + (d1/d2) * vAB
    )
)

fn unit_test=
(
    print ("magnitude [1,2,3]: " + (length [1,2,3]) as string)
    print ("add_ms [1,2,3] [4,5,6]: " + ([1,2,3]+[4,5,6]) as string)
    print ("sub [1,2,3] [4,5,6]: " + ([1,2,3]-[4,5,6]) as string)
    print ("mul [1,2,3] 0.5: " + ([1,2,3]*0.5) as string)
    print ("vec_mul [1,2,3] [3,4,5]: " + ([1,2,3]*[3,4,5]) as string)
    print ("dot_ms [1,2,3] [4,5,6]: " + (dot [1,2,3] [4,5,6]) as string)
    print ("cross_ms [1,2,3] [4,5,6]: " + (cross [1,2,3] [4,5,6]) as string)
    print ("normalize_ms [1,2,3]: " + (normalize [1,2,3]) as string)
    print ("plane_normal [1,2,3] [4,5,6] [1,5,3]: " + (plane_normal [1,2,3] [4,5,6] [1,5,3]) as string)
    print ("distance_ms [1,2,3] [4,5,6]: " + (distance [1,2,3] [4,5,6]) as string)
    print ("alongPoint [1,2,3] [4,5,6] 0.5: " + (alongPoint [1,2,3] [4,5,6] 0.5) as string)
    print ("point_line_projection [1,2,3] [4,5,6] [1,5,3]: " + (point_line_projection [1,2,3] [4,5,6] [1,5,3]) as string)
    print ("point_line_distance [1,2,3] [4,5,6] [1,5,3]: " + (point_line_distance [1,2,3] [4,5,6] [1,5,3]) as string)
    print ("is_point_on_line [1,2,3] [4,5,6] [7,8,9]: " + (is_point_on_line [1,2,3] [4,5,6] [7,8,9] 0.1) as string)
    print ("is_point_on_line [1,2,3] [4,5,6] [1,5,3]: " + (is_point_on_line [1,2,3] [4,5,6] [1,5,3] 0.1) as string)
    print ("line_line_intersect([1,2,3], [1,0,0], [4,5,6], [0,1,0]): " + (line_line_intersect [1,2,3] [1,0,0] [4,5,6] [0,1,0]) as string)
    print ("plane_line_intersect [1,2,3] [1,0,0] [1,2,3] [4,5,6]: " + (plane_line_intersect [1,2,3] [1,0,0] [1,2,3] [4,5,6]) as string)
)

unit_test()
