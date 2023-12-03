def bubble_sort(data):
    n = len(data)
    for i in range(n):
        for j in range(0, n-i-1):
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]
                yield data, [j, j+1]  # Yield the array and the swapped indices
    yield data, []  # Yield the final array with no highlighted index
