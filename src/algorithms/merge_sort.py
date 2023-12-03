# algorithms/merge_sort.py

def merge_sort(data):
    if len(data) > 1:
        mid = len(data) // 2
        left_half = data[:mid]
        right_half = data[mid:]

        yield from merge_sort(left_half)
        yield from merge_sort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                data[k] = left_half[i]
                i += 1
            else:
                data[k] = right_half[j]
                j += 1
            k += 1
            yield data

        while i < len(left_half):
            data[k] = left_half[i]
            i += 1
            k += 1
            yield data

        while j < len(right_half):
            data[k] = right_half[j]
            j += 1
            k += 1
            yield data
