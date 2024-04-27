#include <stdio.h>
#include <string.h>
int main(){
    char s[101];
    scanf("%s",s);
    for(char c='a';c<='z';c++) {
        char *p=strchr(s,c);
        printf("%d ",p?p-s:-1);
    }
}