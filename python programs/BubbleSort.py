# Bubble Sort

def bubbleSort(arr):
    n = len(arr)
    for i in range(0, n):
        for j in range(i + 1, n):
            # swapping condition
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
            else:
                pass
