#include <stdio.h>

int IsMultiple(int a, int b)
{
    if (a % b == 0)
        return 1;
    else
        return 0;
    //! if b%a == 0, then a is a multiple of b
    // Example: a=10 and b=5 then b%a == 0 and 5 x 2 = 10 which is a multiple of 10
}
int main()
{
    int num1, num2;
    scanf("%d %d", &num1, &num2);
    printf("%d\n", IsMultiple(num1, num2));
}

// Write a C program using function that determines for a pair of integers whether the second integer is a multiple of the first. The function should take two integer arguments and return 1 (true) if the second is a multiple of the first, and 0 (false) otherwise. Use this function in a program that inputs a series of pairs of integers.