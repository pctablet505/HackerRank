#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() 
{

    int n;
    scanf("%d", &n);
    int arr[2*n-1][2*n-1];
    for (int i=n;i>0;i--){
        for(int j=n-i;j<n+i-1;j++){
            arr[n-i][j]=i;
            arr[j][n-i]=i;
            arr[j][n+i-2]=i;
            arr[n+i-2][j]=i;
        }
    }
    for(int i=0;i<2*n-1;i++){
        for(int j=0;j<2*n-1;j++){
            printf("%d ",arr[i][j]);
        }
        printf("\n");
    }
    
    return 0;
}
