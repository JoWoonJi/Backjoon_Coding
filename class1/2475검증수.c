#include <stdio.h>
int main(){
    int x=0,n,i;
    for (i=0;i<5;i++){
        scanf("%d",&n);
        x += n*n;
    }
    printf("%d",x%10);
    return 0;
}