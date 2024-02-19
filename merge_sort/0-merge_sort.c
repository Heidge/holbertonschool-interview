#include <stdio.h>
#include <stdlib.h>
#include "sort.h"



void merge(int *array, int left, int middle, int right) {
    int i, j, k;
    int n1 = middle - left + 1;
    int n2 = right - middle;

    // Allocate a single temporary array for both left and right subarrays
    int *temp_array = (int *)malloc((n1 + n2) * sizeof(int));

    i = 0;
    j = 0;
    k = left;

    // Copy data to temp_array
    for (int idx = 0; idx < n1; idx++)
        temp_array[idx] = array[left + idx];
    for (int idx = 0; idx < n2; idx++)
        temp_array[n1 + idx] = array[middle + 1 + idx];

    // Merge the two subarrays back into array
    while (i < n1 && j < n2) {
        if (temp_array[i] <= temp_array[n1 + j]) {
            array[k] = temp_array[i];
            i++;
        } else {
            array[k] = temp_array[n1 + j];
            j++;
        }
        k++;
    }

    // Copy the remaining elements of left_array to array
    while (i < n1) {
        array[k] = temp_array[i];
        i++;
        k++;
    }

    // Copy the remaining elements of right_array to array
    while (j < n2) {
        array[k] = temp_array[n1 + j];
        j++;
        k++;
    }

    // Free the temporary array
    free(temp_array);
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
