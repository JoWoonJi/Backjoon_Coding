#include <stdio.h>
#include <limits.h>
int main(){
    int n,i,min=INT_MAX,max=INT_MIN;
    scanf("%d",&n);
    int l[n];
    for (i=0;i<n;i++){
        scanf("%d",&l[i]);
    }
    for (i=0;i<n;i++){
        if (l[i]<min){
            min=l[i];
        }
        if (l[i]>max){
            max=l[i];
        }
    }
    printf("%d %d",min,max);
}