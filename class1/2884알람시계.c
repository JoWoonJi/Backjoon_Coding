#include <stdio.h>
int main(){
    int h,m;
    scanf("%d %d",&h,&m);
    if (m<45){
        h=(h+23)%24;
        m+=15;
    }
    else{
        m-=45;
    }
    printf("%d %d",h,m);
}