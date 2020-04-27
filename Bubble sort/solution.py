#!/local/usr/bin/python3

"""
better case: O(N)
medium case: O(Nˆ2)
worst case: O(Nˆ2)
"""

def solution(arr, N):
	if not N:
		return arr
	for i in range(N-1):
		if arr[i] > arr[i+1]:
			swap = arr[i]
			arr[i] = arr[i+1]
			arr[i+1] = swap

	solution(arr, N-1)

arr = [3,4,2,20,3,5,9,8,12]
solution(arr, len(arr))
