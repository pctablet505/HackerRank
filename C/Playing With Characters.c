#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() {

    char ch;
    char c[20];
    char s[200];
    scanf("%c", &ch);
    scanf("%s", &c);
    scanf("\n%[^\n]%*c", &s);
    printf("%c\n", ch);
    printf("%s\n", c);
    printf("%s", s);
    return 0;
}

