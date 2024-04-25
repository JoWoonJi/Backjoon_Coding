#include <stdio.h>
int main(){
    int n,x[42]={0},i,cnt=0;
    for (i=0;i<10;i++){
        scanf("%d",&n);
        if (x[n%42]==0){
            x[n%42]=1;
            cnt++;
        }
    }
    printf("%d",cnt);
}