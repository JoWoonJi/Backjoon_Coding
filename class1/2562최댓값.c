#include <stdio.h>
int main(){
    int n[9],m=-1,idx=0,i;
    for (i=0;i<9;i++){
        scanf("%d",&n[i]);
        if (n[i]>m){
            m=n[i];
            idx=i;
        }
    }
    printf("%d\n",m);
    printf("%d",idx+1);
}