#include <stdio.h>
int main(){
    int a = 5;
    int b = 3;
    int c = 10;
    if((a < b) && (c < a)){
        printf("1");
    } 
    else if((b > a || c % 2 == 0) && a == 1){
        printf("2");
    }
    else if(c > 12){
        printf("3");
    }
    else{
        printf("4");
    }
}