#!/local/usr/bin/python3

"""
better case: O(N)
medium case: O(Nˆ2)
worst case: O(Nˆ2)
"""

def solution(arr):
	size_arr = len(arr)
	for i in range(size_arr-1):
		for j in range(i+1, 0, -1):
			if arr[j-1] > arr[j]:
				aux = arr[j-1]
				arr[j-1] = arr[j]
				arr[j] = aux
			else:
				break

	return arr

print(solution([10,5,3,20,6,9,1]))
