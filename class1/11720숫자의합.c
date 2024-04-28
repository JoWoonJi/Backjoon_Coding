#include <stdio.h>
int main(){
    int n,i,s=0;
    char x[101];
    scanf("%d",&n);
    scanf("%s",x);
    for (i=0;i<n;i++){
        s+=x[i]-'0';
    }
    printf("%d",s);
}