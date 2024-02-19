#include <stdio.h>
#include <stdlib.h>
#include "sort.h"


void merge(int *array, int left, int middle, int right) {
    int i, j, k;
    int n1 = middle - left + 1;
    int n2 = right - middle;

    int *left_array = (int *)malloc(n1 * sizeof(int));
    int *right_array = (int *)malloc(n2 * sizeof(int));

    for (i = 0; i < n1; i++)
        left_array[i] = array[left + i];
    for (j = 0; j < n2; j++)
        right_array[j] = array[middle + 1 + j];

    i = 0;
    j = 0;
    k = left;
    while (i < n1 && j < n2) {
        if (left_array[i] <= right_array[j]) {
            array[k] = left_array[i];
            i++;
        } else {
            array[k] = right_array[j];
            j++;
        }
        k++;
    }

    while (i < n1) {
        array[k] = left_array[i];
        i++;
        k++;
    }

    while (j < n2) {
        array[k] = right_array[j];
        j++;
        k++;
    }

    free(left_array);
    free(right_array);
}

void merge_sort_helper(int *array, int left, int right) {
    if (left < right) {
        int middle = left + (right - left) / 2;

        merge_sort_helper(array, left, middle);
        merge_sort_helper(array, middle + 1, right);

        printf("Merging...\n");
        printf("[left]: ");
        print_array(array + left, middle - left + 1);
        printf("[right]: ");
        print_array(array + middle + 1, right - middle);
        printf("\n");

        merge(array, left, middle, right);

        printf("[Done]: ");
        print_array(array + left, right - left + 1);
    }
}

void merge_sort(int *array, size_t size) {
    merge_sort_helper(array, 0, size - 1);
}
