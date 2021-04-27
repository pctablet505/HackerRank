#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>


int main() {
    int a, b;
    scanf("%d\n%d", &a, &b);
    // Complete the code.
    int i;
    for (i = a; i <= b; i++) {

        if (i == 0)
            puts("zero");
        if (i == 1)
            puts("one");
        if (i == 2)
            puts("two");
        if (i == 3)
            puts("three");
        if (i == 4)
            puts("four");
        if (i == 5)
            puts("five");
        if (i == 6)
            puts("six");
        if (i == 7)
            puts("seven");
        if (i == 8)
            puts("eight");
        if (i == 9)
            puts("nine");
        if (i > 9 && i % 2 == 0)
            puts("even");
        if (i > 9 && i % 2 == 1)
            puts("odd");
    }


    return 0;
}


