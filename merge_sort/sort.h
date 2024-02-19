#ifndef _LISTS_H_
#define _LISTS_H_

#include <stddef.h>

void merge(int *array, int left, int mid, int right);
void merge_sort_helper(int *array, int left, int right);
void merge_sort(int *array, size_t size);
void print_array(const int *array, size_t size);

#endif