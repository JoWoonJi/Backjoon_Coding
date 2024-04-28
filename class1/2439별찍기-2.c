#include <stdio.h>
int main(){
    int n,i,j;
    scanf("%d",&n);
    for (i=1;i<n+1;i++){
        for (j=1;j<=n-i;j++){
            printf(" ");
        }
        for (j=1;j<=i;j++){
            printf("*");
        }
        printf("\n");
        }
}


// #include <stdio.h>
// int main() {
//     int N,i,j;
//     scanf("%d",&N);
//     for (i=1;i<=N;i++){
//         for (j=1;j<=N;j++){
//             printf("%s",j<=N-i?" ":"*");
//         }
//         printf("\n");
//     }
// }