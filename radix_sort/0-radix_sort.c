#include <stdlib.h>
#include <stdio.h>
#include <math.h>
#include "sort.h"

int numLength(int num) 
{
    int count = 0;

    while (num > 0) {
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

void radix_sort(int *array, size_t size) 
{
    int i = 0;
    int j = 0;
    int k = 0;
    int len = size;
    int duration = numLength(getMax(array, size));
    
    int *tmp_array = (int *)malloc(len * sizeof(int));

    if (tmp_array == NULL) 
    {
        fprintf(stderr, "Erreur d'allocation mémoire\n");
        exit(EXIT_FAILURE);
    }

    for (; j < duration; j++) 
    {
        if (j == 0) 
        {
            for (i = 0; i < len; i++) {
                for (k = 0; k < len; k++) {
                    if (array[k] % 10 > array[i] % 10) {
                        tmp_array[k] = array[k];
                        array[k] = array[i];
                        array[i] = tmp_array[k];
                    }
                }
            }
        } 
        else 
        {
            for (i = 0; i < len; i++) {
                for (k = 0; k < len; k++) {
                    if (array[k] / pow(10, i) > array[i] / pow(10, i)) {
                        tmp_array[k] = array[k];
                        array[k] = array[i];
                        array[i] = tmp_array[k];
                    }
                }
            }
        }
        print_array(array, size);
    }

    free(tmp_array);
}

