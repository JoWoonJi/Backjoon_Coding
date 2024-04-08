#include <stdio.h>
int main(){
    int n,x,l[n],i;
    scanf("%d %d",&n,&x);
    for (i=0;i<n;i++){
        scanf("%d",&l[i]);
    }
    for (i=0;i<n;i++){
        if (l[i]<x){
            printf("%d ",l[i]);
        }
    }
}

//더 간결하게 
// #include <stdio.h>
// int main(){
//     int n,x,l,i;
//     scanf("%d %d",&n,&x);
//     for (i=0;i<n;i++){
//         scanf("%d",&l);
//         if (l<x) {
//             printf("%d ",l);
//         }
//     }
// }