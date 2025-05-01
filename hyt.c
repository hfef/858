#include <stdio.h>
// 定义一个结构体，用于存储 d200 和 d100
typedef struct {
    int d200;
    int d100;
} app;

// 函数：打印结构体中的数据
void printData(app bbu) {
    printf("d200: %d, d100: %d\n", bbu.d200, bbu.d100);
}

// 函数：将两个变量相加并返回结果
int sumData(app *data) {
    
    printf("Sum: %d\n", data->d200 + data->d100);
    return 0;
}

int main() {
    
    // 初始化结构体数据
    app bbu = {200, 100};

    // 打印结构体数据
    printData(bbu);
 
    // 计算并打印两个变量的和
    int total = sumData(&bbu);
    printf("Sum of d200 and d100: %d\n", total);
    return 0;
    }










































