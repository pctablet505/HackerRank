#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() {
    int count[] = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0};
    char s[1000];
    char *c = s;
    scanf("%s", &s);


    while (*c) {
        if (*c >= '0' && *c <= '9') {
            count[*c - '0'] += 1;
        }
        c++;
    }
    for (int i = 0; i < 10; i++) {
        printf("%d ", count[i]);
    }


    /* Enter your code here. Read input from STDIN. Print output to STDOUT */
    return 0;
}
