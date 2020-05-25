#!/usr/local/bin/pytho3

"""
better case: O(N * log N)
medium case: O(N * log N)
worst case: O(N^2)
"""


def partition(arr, init, end):
	pivot = arr[end]
	position = init - 1
	for j in range(init, end + 1):
		if arr[j] <= pivot:  # swap
			position += 1
			aux = arr[position]
			arr[position] = arr[j]
			arr[j] = aux

	return position


def quick_sort(arr, init, end):
	if init < end:
		middle = partition(arr, init, end)
		quick_sort(arr, init, middle-1)
		quick_sort(arr, middle+1, end)


arr = [10,5,8,20,9,1,5]
quick_sort(arr, 0, 6)
print(arr)

