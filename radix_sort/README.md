# Radix Sort

## More info

#include <stdlib.h>
#include <stdio.h>

void print_array(const int *array, size_t size)
{
    size_t i;

    i = 0;
    while (array && i < size)
    {
        if (i > 0)
            printf(", ");
        printf("%d", array[i]);
        ++i;
    }
    printf("\n");
}

- Our file print_array.c will be compiled with your function during the correction.
- Please declare the prototype of the function print_array in your sort.h header file

## Tasks

### 0. Radix sort

Write a function that sorts an array of integers in ascending order using the Radix sort algorithm

- Prototype: void radix_sort(int *array, size_t size);
- You must implement the LSD radix sort algorithm
- You can assume that array will contain only numbers >= 0
- You are allowed to use malloc and free for this task
- You’re expected to print the array each time you increase your significant digit (See example below)

