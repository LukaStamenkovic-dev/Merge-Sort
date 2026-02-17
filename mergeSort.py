
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

l = [2, 4, 2, 1, 6, 6, 4, 9]
sorted = merge_sort(l)
print(sorted)