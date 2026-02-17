import timeit
import random

def insertion_sort(array):
    for i in range(1, len(array)):
        current_element = array[i]
        j = i - 1
        while j >= 0 and current_element < array[j]:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = current_element
    return array

def merge_sort(array):
    if len(array) <= 1:
        return array
    else:
        left_split = array[:len(array)// 2]
        right_split = array[len(array)//2:]
        left = merge_sort(left_split)
        right = merge_sort(right_split)
        return merge(left, right)
    
def merge(left, right):
    merged = []

    left_pointer = 0
    right_pointer = 0

    merging = True
    while merging:
        left_element = left[left_pointer]
        right_element = right[right_pointer]
        if left_element < right_element:
            merged.append(left_element)
            left_pointer += 1
        elif right_element < left_element:
            merged.append(right_element)
            right_pointer += 1
        else:
            merged.append(left_element)
            merged.append(right_element)
            left_pointer += 1
            right_pointer += 1
        
        if left_pointer >= len(left):
            merged.extend(right[right_pointer:])
            merging = False
        elif right_pointer >= len(right):
            merged.extend(left[left_pointer:])
            merging = False
    
    return merged


l = [random.randint(1, 1000) for _ in range(10000)]
insertion_time = timeit.timeit(lambda: insertion_sort(l), number=5)
merge_time = timeit.timeit(lambda: merge_sort(l), number=5)

print(f"Insertion time: {insertion_time:.6} seconds")
print(f'Merge time: {merge_time:.6} seconds')