#include <stdio.h>

int max_of_four(int, int, int, int);

/*
Add `int max_of_four(int a, int b, int c, int d)` here.
*/

int main() {
    int a, b, c, d;
    scanf("%d %d %d %d", &a, &b, &c, &d);
    int ans = max_of_four(a, b, c, d);
    printf("%d", ans);

    return 0;
}

max_of_four(int a, int b, int c, int d) {
    int max = d;
    if (a > b && a > c && a > d)
        max = a;
    if (b > a && b > c && b > d)
        max = b;
    if (c > b && c > a && c > d)
        max = c;
    return max;
}

