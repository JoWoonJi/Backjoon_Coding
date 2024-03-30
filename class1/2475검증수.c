#include <stdio.h>
int main(){
    int n[5];
    int x=0;
    int i;
    for (i=0;i<5;i++){
        scanf("%d",&n[i]);
    }
    for (i=0;i<5;i++){
        x += n[i]*n[i];
    }
    printf("%d",x%10);
    return 0;
}