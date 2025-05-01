#include<stdio.h>
typedef struct {
    int hd45;
    int hd44;
    int hd43;
}app;
app bbu ={22,54,2};
void main(app*inc){
printf("HD44:%D",inc->hd44);
}     