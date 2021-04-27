#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() {

    char *s;
    s = malloc(1024 * sizeof(char));
    scanf("%[^\n]", s);
    //Write your logic to print the tokens of the sentence here.
    char *c=s;
    int i=0,j=0;
    while(*c!=NULL){
        printf("%c",*c);
        c+=1;
        if( *c==' '){
            printf("\n");
            c+=1;
        }
    }
    return 0;
}
