# Heap Extract

## More Info

### Data structures

Please use the following data structures and types for binary trees. Don’t forget to include them in your header file.

#### Basic Binary Tree

/**
 \* struct binary_tree_s - Binary tree node
 *
 \* @n: Integer stored in the node
 \* @parent: Pointer to the parent node
 \* @left: Pointer to the left child node
 \* @right: Pointer to the right child node
 */
struct binary_tree_sv
{
    int n;
    struct binary_tree_s *parent;
    struct binary_tree_s *left;
    struct binary_tree_s *right;
};

typedef struct binary_tree_s binary_tree_t;

#### Max Binary Heap

typedef struct binary_tree_s heap_t;

### Print function

To match the examples in the tasks, you are given [this function](https://github.com/hs-hq/0x1C.c)

This function is used only for visualisation purpose. You don’t have to push it to your repo. It may not be used during the correction

## Tasks

### 0. Heap - Extract

Write a function that extracts the root node of a Max Binary Heap:

- Prototype: int heap_extract(heap_t **root);
- root is a double pointer to the root node of the heap
- Your function must return the value stored in the root node
- The root node must be freed and replace with the last level-order node of the heap
- Once replaced, the heap must be rebuilt if necessary
- If your function fails, return 0

Note: In order for the main file to compile, you are provided with this static library. This library won’t be used during correction, its only purpose is for testing.
