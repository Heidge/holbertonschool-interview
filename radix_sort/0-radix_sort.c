#include <stdlib.h>
#include <stdio.h>
#include <math.h>
#include "sort.h"

int numLength(int num) 
{
    int count = 0;

    while (num > 0) 
    {
        count++;
        num = num / 10;
    }
    return count;
}

int getMax(int *array, int n) 
{
    int i = 0;
    int mx = array[0];
    for (i = 1; i < n; i++)
        if (array[i] > mx)
            mx = array[i];
    return mx;
}

int my_pow(int base, int exponent) 
{
    int result = 1.0;
    int i;
    
    if (exponent < 0) 
    {
        base = 1.0 / base;
        exponent = -exponent;
    }
    
    for (i = 0; i < exponent; i++) 
    {
        result *= base;
    }
    
    return result;
}

void radix_sort(int *array, size_t size) {
    int i, j;
    int len = size;
    int duration = numLength(getMax(array, size));
    
    int *tmp_array = (int *)malloc(len * sizeof(int));

    if (tmp_array == NULL) {
        fprintf(stderr, "Erreur d'allocation mémoire\n");
        exit(EXIT_FAILURE);
    }

    for (j = 0; j < duration; j++) {
        for (i = 0; i < len; i++) {
            tmp_array[i] = array[i];
        }

        int count[10] = {0};
        int output[len];

        for (i = 0; i < len; i++) {
            count[(tmp_array[i] / my_pow(10, j)) % 10]++;
        }

        for (i = 1; i < 10; i++) {
            count[i] += count[i - 1];
        }

        for (i = len - 1; i >= 0; i--) {
            output[count[(tmp_array[i] / my_pow(10, j)) % 10] - 1] = tmp_array[i];
            count[(tmp_array[i] / my_pow(10, j)) % 10]--;
        }

        for (i = 0; i < len; i++) {
            array[i] = output[i];
        }

        print_array(array, size);
    }

    free(tmp_array);
}

