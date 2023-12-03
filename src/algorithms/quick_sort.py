# algorithms/quick_sort.py

def quick_sort(data):
    if len(data) <= 1:
        yield data
    else:
        pivot = data[len(data) // 2]
        less = []
        equal = []
        greater = []
        for x in data:
            if x < pivot:
                less.append(x)
            elif x == pivot:
                equal.append(x)
            else:
                greater.append(x)
        for part in quick_sort(less):
            yield part + equal + greater
        for part in quick_sort(greater):
            yield less + equal + part
