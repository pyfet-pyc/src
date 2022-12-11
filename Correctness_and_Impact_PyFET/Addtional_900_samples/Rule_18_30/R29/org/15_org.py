def heapSort(arr):
    n = len(arr)

    # Build a maxheap.
    # Since last parent will be at ((n//2)-1) we can start at that location.
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # One by one extract elements
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # swap
        heapify(arr, i, 0)


    # Driver code to test above
    arr = [12, 11, 13, 5, 6, 7]
    heapSort(arr)
    n = len(arr)
    print("Sorted array is")
    for i in range(n):
        print("%d" % arr[i]),