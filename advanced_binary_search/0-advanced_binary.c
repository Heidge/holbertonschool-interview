#include <stdio.h>
#include "search_algos.h"

/**
 * advanced_binary_recursive - Recursive helper function for advanced_binary
 * @array: Pointer to the first element of the array to search in
 * @left: Index of the left bound of the subarray
 * @right: Index of the right bound of the subarray
 * @value: The value to search for
 *
 * Return: Index where the value is located, or -1 if not found
 */
int advanced_binary_recursive(int *array, size_t left, size_t right, int value);

/**
 * advanced_binary - Searches for a value in a sorted array using binary search
 * @array: Pointer to the first element of the array to search in
 * @size: Number of elements in array
 * @value: The value to search for
 *
 * Return: Index where the value is located, or -1 if not found
 */
int advanced_binary(int *array, size_t size, int value) 
{
    if (array == NULL || size == 0) 
    {
        return -1;
    }

    return advanced_binary_recursive(array, 0, size - 1, value);
}

/**
 * advanced_binary_recursive - Recursive helper function for advanced_binary
 * @array: Pointer to the first element of the array to search in
 * @left: Index of the left bound of the subarray
 * @right: Index of the right bound of the subarray
 * @value: The value to search for
 *
 * Return: Index where the value is located, or -1 if not found
 */
int advanced_binary_recursive(int *array, size_t left, size_t right, int value) 
{
    if (left <= right) 
    {
        size_t i = 0;
        size_t mid = left + (right - left) / 2;

        printf("Searching in array: ");
        for (i = left; i <= right; ++i) 
        {
            printf("%d", array[i]);
            if (i < right) 
            {
                printf(", ");
            }
        }
        printf("\n");

        if (array[mid] == value) 
        {
            if (mid == left || array[mid - 1] != value) 
            {
                return mid;
            }
            else 
            {
                return advanced_binary_recursive(array, left, mid, value);
            }
        }
        else if (array[mid] < value) 
        {
            return advanced_binary_recursive(array, mid + 1, right, value);
        }
        else 
        {
            return advanced_binary_recursive(array, left, mid - 1, value);
        }
    }

    return -1;
}
