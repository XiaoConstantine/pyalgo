package main

import "fmt"

func merge_two_sorted_arrs(arr1 []int, arr2 []int) []int {
	results := make([]int, len(arr1)+len(arr2))
	i, j, k := 0, 0, 0
	for i < len(arr1) && j < len(arr2) {
		if arr1[i] > arr2[j] {
			results[k] = arr2[j]
			j++
		} else {
			results[k] = arr1[i]
			i++
		}
		k++
	}
	for ; i < len(arr1); i++ {
		results[k] = arr1[i]
		k++
	}

	for ; j < len(arr2); j++ {
		results[k] = arr2[j]
		k++
	}
	return results
}

func merge_sort(arr []int) []int {
	// how does merge sort work
	// guess basic idea is recursive dq
	if len(arr) == 1 {
		return []int{arr[0]}
	} else if len(arr) == 2 {
		if arr[0] > arr[1] {
			return []int{arr[1], arr[0]}
		} else {
			return []int{arr[0], arr[1]}
		}
	}
	start, end := 0, len(arr)-1
	mid := start + (end-start)/2
	left_sub := merge_sort(arr[:mid])
	right_sub := merge_sort(arr[mid:])

	return merge_two_sorted_arrs(left_sub, right_sub)
}

func main() {
	arr := []int{5, 2, 2, 4, 1, 3, 9}
	fmt.Println(merge_sort(arr))
}
