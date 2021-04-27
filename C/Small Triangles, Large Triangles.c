
double area(triangle tri) {
    double s = (tri.a + tri.b + tri.c) / 2.0;
    float ar = sqrt(s * (s - tri.a) * (s - tri.b) * (s - tri.c));
    return -1 * ar;
}

int comp(triangle *a, triangle *b) {
    return area(*a) < area(*b);
}

void sort_by_area(triangle *tr, int n) {
    qsort((void *) tr, n, sizeof(triangle), comp);
}

