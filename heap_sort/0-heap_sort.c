#include "sort.h"

void swap(int *a, int *b)
{
    int tmp = *a;
    *a = *b;
    *b = tmp;
}

void heapify(int arr[], int N, int i)
{
    int largest = i;
    int l = 2 * i + 1;
    int r = 2 * i + 2;

    if (l < N && arr[l] > arr[largest])
        largest = l;

    if (r < N && arr[r] > arr[largest])
        largest = r;

    if (largest != i) {
        swap(&arr[i], &arr[largest]);
        heapify(arr, N, largest);
    }
}

void heap_sort(int *array, size_t size)
{
    int a = size / 2 - 1;
    int b = size - 1;
    int i = 0;
    int y = 0;

    for (int i = a; i >= 0; i--) {
        heapify(array, size, i);
    }

    for (int y = b; y >= 0; y--) {
        swap(&array[0], &array[y]);
        
        heapify(array, y, 0);
        print_array(array, size);
    }
}