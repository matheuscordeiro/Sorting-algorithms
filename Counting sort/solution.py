#!/usr/local/bin/python3

"""
better case: O(N + k)
medium case: O(N + k)
worst case: O(N + k)
"""

def solution(arr, k):
	count_arr = [0] * k
	for i in arr:
		count_arr[i] += 1

	for i in range(1, k):
		count_arr[i] += count_arr[i-1]

	size_arr = len(arr)
	sorted_arr = [0] * size_arr
	for i in range(size_arr):
		value = arr[i]
		position = count_arr[value] - 1
		sorted_arr[position] = value
		count_arr[value] -= 1

	return sorted_arr
