#ifndef LISTS_H
#define LISTS_H

#include <stdlib.h>
#include <stdio.h>

void print_array(const int *array, size_t size);
void swap(int* a, int* b);
void heapify(int arr[], int N, int i);
void heap_sort(int *array, size_t size);

#endif /* LISTS_H */
