#include <stdio.h>
int main(){
    int n;
    scanf("%d",&n);
    if (89<n&&n<101){
        printf("A");
    }
    else if(79<n&&n<90){
        printf("B");
    }
    else if(69<n&&n<80){
        printf("C");
    }
    else if(59<n&&n<70){
        printf("D");
    }
    else{
        printf("F");
    }
}