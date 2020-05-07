#include "remove_duplicates.h"

// Function to remove duplicated elements in an array
void remove_duplicates(const unsigned int *vin, unsigned int *vout, const unsigned int size)
{
    /*
    
        Complexity Analysis
        ---------------------------------------------
        TIME                     O(n * log(n)) + O(n) = O(n * log(n))
        SPACE                    O(n) + O(1) = O(n)
        ---------------------------------------------
        
    */    
    
    // Creating copy of the entry vector... (good choice)
    unsigned int arr[size];
    for(int i = 0; i < size; i++)
    {
        arr[i] = vim[i];
    }
    
    // Sorting the array with the heap-sort algorithm
    heap_sort(arr, size);
    
    int i = 0;
    int j = 0;
    while (i < n)
    {
        // Insert element to the result vector
        vout[j] = vin[i];
        j = j + 1;
        
        while (vin[i] == vin[i + 1])
        {
            i = i + 1;
        }  
        i = i + 1;
    }
}

// Heap-sort main function
void heap_sort(unsigned int arr[], const unsigned int size)
{
    /*
    
        Complexity Analysis
        ---------------------------------------------
        best, worst, average TIME      O(n * log(n))
        SPACE                          O(1)
        ---------------------------------------------
        
    */
    
    for (unsigned int i = size / 2 - 1; i >= 0; i--)
    {
        create_max_heap(arr, size, i); 
    }
        
    for (unsigned int i = size - 1; i > 0; i--) 
    { 
        swap(arr[0], arr[i]); 
        create_max_heap(arr, i, 0);
    } 
}

// Heap-sort helper function
void create_max_heap(unsigned int arr[], const unsigned int size, unsigned int root_index)
{
    unsigned int root = root_index;
    unsigned int left = 2 * root + 1;
    unsigned int right = 2 * root + 2;
    
    // If the left son is greater than the root
    if (left < size && arr[left] > arr[root])
    {
        root = left;
    }
    
    // If the right son is greater than the root
    if (right < size && arr[right] > arr[root])
    {
        root = right;
    }
    
    // If the root has changed
    if (root != root_index)
    {
        swap_nodes(arr[root], arr[root_index]);
        
        // Continue resolving the new tree
        create_max_heap(arr,  size, root);
    }
}

// Heap-sort helper function
void swap_nodes(unsigned int *ptr1, unsigned int *ptr2)
{
    unsigned int tmp = *ptr1;
    *ptr1 = *ptr2;
    *ptr2 = tmp;
}