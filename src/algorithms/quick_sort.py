import simpleaudio as sa

swap_sound = sa.WaveObject.from_wave_file("../1417.wav")

def play_sound():
    swap_sound.play()



def quick_sort(data, start=0, end=None):
    if end is None:
        end = len(data)

    if end - start > 1:
        pivot_index = start
        pivot = data[pivot_index]
        low = start + 1
        high = end - 1

        while True:
            while low <= high and data[high] >= pivot:
                high = high - 1

            while low <= high and data[low] <= pivot:
                low = low + 1

            if low <= high:
                data[low], data[high] = data[high], data[low]
                play_sound()
                yield data, [low, high]  # Yield array and swapped indices
            else:
                break

        data[start], data[high] = data[high], data[start]
        yield data, [start, high]  # Yield array and swapped indices for pivot

        yield from quick_sort(data, start, high)
        yield from quick_sort(data, high + 1, end)
