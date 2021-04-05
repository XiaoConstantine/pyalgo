# Conceptually, a merge sort works as follows:
# Divide the unsorted list into n sublists, each containing one element (a list of one element is considered sorted).
# Repeatedly merge sublists to produce new sorted sublists until there is only one sublist remaining. This will be the sorted list.
def merge_sort(arr):
    if len(arr) == 0 or len(arr) == 1:
        return arr
    elif len(arr) == 2:
        if arr[0] > arr[1]:
            return [arr[1], arr[0]]
        else:
            return arr
    else:
        s, e = 0, len(arr) - 1
        mid = (s + e) // 2
        left = merge_sort(arr[:mid])
        right = merge_sort(arr[mid:])
        # merge left and right
        # how to merge two sorted lists
        # 3 pointer
        # for example:
        # u got left: [4], right: [4, 6]
        # result gonna contain 3 elements: [4, 4, 6]
        result_index, left_index, right_index = 0, 0, 0
        result = [None] * (len(left) + len(right))

        while left_index < len(left) and right_index < len(right):
            if left[left_index] < right[right_index]:
                result[result_index] = left[left_index]
                left_index += 1
            else:
                result[result_index] = right[right_index]
                right_index += 1
            result_index += 1
        
        while left_index < len(left):
            result[result_index] = left[left_index]
            result_index += 1
            left_index += 1

        while right_index < len(right):
            result[result_index] = right[right_index]
            result_index += 1
            right_index += 1
 
        return result
        
if __name__ == "__main__":
    c = [5,9,1,3,4,6,6,3,2]
    # [5,9,1,3]  [4,6,6,3,2]
    # [5], [9, 1, 3], [4,6], [6,3,2]  
    # [5], [9], [1,3], [4, 6], [6], [2,3]
    # c = [2,2,2]
    result = [1,2,3,3,4,5,6,6,9]
    assert result == merge_sort(c)
