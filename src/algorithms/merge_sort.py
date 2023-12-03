def merge_sort(data, start=0, end=None):
    if end is None:
        end = len(data)
    if end - start > 1:
        mid = (start + end) // 2
        yield from merge_sort(data, start, mid)
        yield from merge_sort(data, mid, end)
        left = data[start:mid]
        right = data[mid:end]
        i = j = 0
        k = start

        merged_indices = []  # List to keep track of merged elements

        while i < len(left) and j < len(right):
            merged_indices.append(k)
            if left[i] < right[j]:
                data[k] = left[i]
                i += 1
            else:
                data[k] = right[j]
                j += 1
            k += 1
            if len(merged_indices) == 2:  # Yield every pair of elements merged
                yield data, merged_indices
                merged_indices = []

        while i < len(left):
            merged_indices.append(k)
            data[k] = left[i]
            i += 1
            k += 1
            if len(merged_indices) == 2:
                yield data, merged_indices
                merged_indices = []

        while j < len(right):
            merged_indices.append(k)
            data[k] = right[j]
            j += 1
            k += 1
            if len(merged_indices) == 2:
                yield data, merged_indices
                merged_indices = []

        if merged_indices:  # Yield any remaining elements
            yield data, merged_indices
