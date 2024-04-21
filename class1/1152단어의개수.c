#include <stdio.h>
int main(){
    char s[1000001];
    int cnt=0;
    while (scanf("%s",s)==1){
        cnt++;
    }
    printf("%d",cnt);
}