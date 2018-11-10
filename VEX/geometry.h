
// Normal of a plane defined by three points pA, pB, pC
vector plane_normal(vector pA, pB, pC) {
    return normalize(cross((pB-pA), (pC-pA)));
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

// Intersection between two lines defined by a point (pA, pB) and a vector (a, b)
vector line_line_intersect(vector pA, a, pB, b) {
    vector c = pB-pA;
    vector cross1 = cross(a, b);
    vector cross2 = cross(c, b);
    return pA + a * dot(cross2, cross1) / pow(length(cross1), 2);
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
    printf("magnitude({1,2,3}): %g \n", length({1,2,3}));
    printf("add({1,2,3}, {4,5,6}): %g \n", {1,2,3}+{4,5,6});
    printf("sub({1,2,3}, {4,5,6}): %g \n", {1,2,3}-{4,5,6});
    printf("mul({1,2,3}, 0.5): %g \n", {1,2,3}*0.5);
    printf("vec_mul({1,2,3}, {3,4,5}): %g \n", {1,2,3}*{3,4,5});
    printf("dot({1,2,3}, {4,5,6}): %g \n", dot({1,2,3}, {4,5,6}));
    printf("cross_vex({1,2,3}, {4,5,6}): %g \n", cross({1,2,3}, {4,5,6}));
    printf("normalize_vex({1,2,3}): %g \n", normalize({1,2,3}));
    printf("plane_normal({1,2,3}, {4,5,6}, {1,5,3}): %g \n", plane_normal({1,2,3}, {4,5,6}, {1,5,3}));
    printf("distance_vex({1,2,3}, {4,5,6}): %g \n", distance({1,2,3}, {4,5,6}));
    printf("alongPoint({1,2,3}, {4,5,6}, 0.25): %g \n", alongPoint({1,2,3}, {4,5,6}, 0.5));
    printf("point_line_projection({1,2,3}, {4,5,6}, {1,5,3}): %g \n", point_line_projection({1,2,3}, {4,5,6}, {1,5,3}));
    printf("point_line_distance({1,2,3}, {4,5,6}, {1,5,3}): %g \n", point_line_distance({1,2,3}, {4,5,6}, {1,5,3}));
    printf("is_point_on_line({1,2,3}, {4,5,6}, {7,8,9}): %g \n", is_point_on_line({1,2,3}, {4,5,6}, {7,8,9}, 0.1));
    printf("is_point_on_line({1,2,3}, {4,5,6}, {1,5,3}): %g \n", is_point_on_line({1,2,3}, {4,5,6}, {1,5,3}, 0.1));
    printf("line_line_intersect({1,2,3}, {1,0,0}, {4,5,6}, {0,1,0}): %g \n", line_line_intersect({1,2,3}, {1,0,0}, {4,5,6}, {0,1,0}));
    printf("plane_line_intersect({1,2,3}, {1,0,0}, {1,2,3}, {4,5,6}): %g \n", plane_line_intersect({1,2,3}, {1,0,0}, {1,2,3}, {4,5,6}));
}

unit_test();
