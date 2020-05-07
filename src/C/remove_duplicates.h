#ifndef __REMOVE_DUPLICATES_H__
#define __REMOVE_DUPLICATES_H__

/* Working with memory already reserved by Python! */

// Function Prototypes

void remove_duplicates(const unsigned int *vin,
                       unsigned int *vout,
                       const unsigned int size);               

void heap_sort(unsigned int arr[], const unsigned int size);

void create_max_heap(unsigned int arr[], 
                     const unsigned int size,
                     unsigned int root_index);
                     
void swap_nodes(unsigned int *ptr1, unsigned int *ptr2); 

#endif
