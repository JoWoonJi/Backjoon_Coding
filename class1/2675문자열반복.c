#include <stdio.h>
#include <string.h>
int main(){
    int t,r,i,j;
    char s[21];
    scanf("%d",&t);
    while (t--){
        scanf("%d %s",&r,s);
        for (i=0;s[i]!='\0';i++){
            for (j=0;j<r;j++) {
                printf("%c",s[i]);
            }
        }
        printf("\n");
    }
}