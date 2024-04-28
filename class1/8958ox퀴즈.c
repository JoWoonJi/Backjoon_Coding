#include <stdio.h>
int main(){
    int t,serial,score,i,j;
    char ox[81];
    scanf("%d",&t);
    while(t--){
        scanf("%s",ox);
        serial=0,score=0;
        for(i=0;ox[i]!='\0';i++){
            if(ox[i]=='O'){
                serial++;
                score+=serial;
            }
            else{
                serial=0;
            }
        }
        printf("%d\n",score);
    }
}