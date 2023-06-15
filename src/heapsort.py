from heap.heap import Heap


def Heapsort(array: list[int]) -> list[int]:
    h = Heap(*array)
    i = len(h) - 1
    while i > -1:  # i from n - 1 to 0
        array[i] = h.remove()
        i -= 1
    return array
