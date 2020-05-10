#!/local/usr/bin/python3

"""
better case: O(Nˆ2)
medium case: O(Nˆ2)
worst case: O(Nˆ2)
"""

def solution(arr):
	size_arr = len(arr)
	for i in range(size_arr-1):
		minimum = i
		for j in range(i+1, size_arr):
			if arr[j] < arr[minimum]:
				minimum = j
		aux = arr[i]
		arr[i] = arr[minimum]
		arr[minimum] = aux

	return arr

print(solution([10,5,3,20,6,9,1]))
