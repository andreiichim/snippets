// Magnitude of vector vAB
// Redundant function, added for consistency.
float magnitude(vector vAB) {
    return length(vAB);
}

// vAB + vCD
// Redundant function, added for consistency.
vector add(vector vAB, vCD) {
    return vAB+vCD;
}

// vAB - vCD
// Redundant function, added for consistency.
vector sub(vector vAB, vCD) {
    return vAB-vCD;
}

// vAB * constant c
// Redundant function, added for consistency.
vector mul(vector vAB; float c) {
    return vAB*c;
}

// Dot product of vector vAB and vector vCD
// Redundant function, added for consistency.
float dot_vex(vector vAB, vCD) {
    return dot(vAB, vCD);
}

// Cross product of vector vAB and vector vCD
// Redundant function, added for consistency.
vector cross_vex(vector vAB, vCD) {
    return cross(vAB, vCD);
}

// Normalize vector vAB
// Redundant function, added for consistency.
vector normalize_vex(vector vAB) {
    return normalize(vAB);
}


// Normal of a plane defined by three points pA, pB, pC
vector plane_normal(vector pA, pB, pC) {
    return normalize(cross((pB-pA), (pC-pA)));
}

// Distance between point pA and point pB
float distance_vex(vector pA, pB) {
    return distance(pA, pB);
}

// Point at along% (0-1) between points pA and pB
vector alongPoint(vector pA, pB; float along) {
    return pA+((pB-pA)*along);
}

// Projection of point pC on the line between point pA and point pB
vector point_line_projection(vector pA, pB, pC) {
    vector vAB = pB-pA;
    vector vAC = pC-pA;
    float d = dot(normalize(vAB), normalize(vAC));
    return pA + (vAB * (d * (length(vAC)/length(vAB))));
}

// Distance between point pC and the line between point pA and point pB
float point_line_distance(vector pA, pB, pC) {
    return distance(pC, (point_line_projection(pA, pB, pC)) );
}

// Check if point pC is on the line between point pA and point pB with tolerance
// Returns 1 if the point IS on the line
// Returns -1 if the point IS NOT on the line
int is_point_on_line(vector pA, pB, pC; float tolerance) {
    if (point_line_distance(pA, pB, pC) <= tolerance) {
        return 1;
    }
    else {
        return -1;
    }
}

// Intersection between a line (defined by point pA and vector vAB) and a plane (defined by point pP and normal pN)
vector plane_line_intersect(vector pP, pN, pA, vAB) {
    vector n_vAB = normalize(vAB);
    float d1 = dot((pP-pA), pN);
    float d2 = dot(n_vAB, pN);
    return pA+n_vAB*(d1/d2);
}

void unit_test() {
    printf("\n");
    printf("magnitude({1,2,3}): %g \n", magnitude({1,2,3}));
    printf("add({1,2,3}, {4,5,6}): %g \n", add({1,2,3}, {4,5,6}));
    printf("sub({1,2,3}, {4,5,6}): %g \n", sub({1,2,3}, {4,5,6}));
    printf("mul({1,2,3}, 0.5): %g \n", mul({1,2,3}, 0.5));
    printf("dot({1,2,3}, {4,5,6}): %g \n", dot_vex({1,2,3}, {4,5,6}));
    printf("cross_vex({1,2,3}, {4,5,6}): %g \n", cross_vex({1,2,3}, {4,5,6}));
    printf("normalize_vex({1,2,3}): %g \n", normalize_vex({1,2,3}));
    printf("plane_normal({1,2,3}, {4,5,6}, {1,5,3}): %g \n", plane_normal({1,2,3}, {4,5,6}, {1,5,3}));
    printf("distance_vex({1,2,3}, {4,5,6}): %g \n", distance_vex({1,2,3}, {4,5,6}));
    printf("alongPoint({1,2,3}, {4,5,6}, 0.25): %g \n", alongPoint({1,2,3}, {4,5,6}, 0.5));
    printf("point_line_projection({1,2,3}, {4,5,6}, {1,5,3}): %g \n", point_line_projection({1,2,3}, {4,5,6}, {1,5,3}));
    printf("point_line_distance({1,2,3}, {4,5,6}, {1,5,3}): %g \n", point_line_distance({1,2,3}, {4,5,6}, {1,5,3}));
    printf("is_point_on_line({1,2,3}, {4,5,6}, {7,8,9}): %g \n", is_point_on_line({1,2,3}, {4,5,6}, {7,8,9}, 0.1));
    printf("is_point_on_line({1,2,3}, {4,5,6}, {1,5,3}): %g \n", is_point_on_line({1,2,3}, {4,5,6}, {1,5,3}, 0.1));
    printf("plane_line_intersect({1,2,3}, {1,0,0}, {1,2,3}, {4,5,6}): %g \n", plane_line_intersect({1,2,3}, {1,0,0}, {1,2,3}, {4,5,6}));
}

unit_test();
