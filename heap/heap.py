class Heap():
    def __init__(self, *array: int) -> None:
        self._elem = list(array)
        # i from n//2 to 0
        i = len(array)//2
        while i >= 0:
            self.__down(i)
            i -= 1

    def __len__(self) -> int:
        return len(self._elem)

    def __swap(self, i, j):
        self._elem[i], self._elem[j] = self._elem[j], self._elem[i]

    def __up(self, i: int):
        j = i//2  # round floor
        if j >= 0:
            if self._elem[i] > self._elem[j]:
                self.__swap(i, j)
                self.__up(j)

    def __down(self, i: int):
        j = 2*i
        if j <= len(self) - 1:
            if j < len(self) - 1:
                if self._elem[j] < self._elem[j+1]:
                    j = j+1
            if self._elem[i] < self._elem[j]:
                self.__swap(i, j)
                self.__down(j)

    def alter(self, i: int, value: int):
        if value > self._elem[i]:
            self._elem[i] = value
            self.__up(i)
        elif value < self._elem[i]:
            self._elem[i] = value
            self.__down(i)
        # if equal nothing to do

    def insert(self, value: int):
        self._elem.append(value)
        self.__up(len(self) - 1)

    def remove(self) -> int:
        removed = self._elem[0]
        self._elem[0] = self._elem[-1]  # copy the last one
        self._elem.pop(-1)  # remove it
        self.__down(0)
        return removed


def Heapsort(array: list[int]) -> list[int]:
    h = Heap(*array)
    m = len(h) - 1
    while m > 0:
        array[m] = h.remove()
        m -= 1
    return array
