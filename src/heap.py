class Heap:
    def __init__(self, *array: int, hi=True) -> None:
        """Initialize a Heap object with none or a series of integers.
        """

        if hi:
            self.__elem = list(set(array))
            for _ in range(len(self)//2, -1, -1):
                self.__down(_)
        else:
            self = __Heap_lo(*array)

    def __repr__(self) -> str:  # print(h) -> 1st elem
        if not self.__elem:
            return ''
        return str(self.__elem[0])

    def __bool__(self) -> bool:  # if h: ...
        return bool(self.__elem)

    def __getitem__(self, _index: int) -> int:  # h[i] -> i-th elem
        return self.__elem[_index]

    def __len__(self) -> int:  # len(h) -> n
        return len(self.__elem)

    def __swap(self, i, j) -> None:
        self.__elem[i], self.__elem[j] = self[j], self[i]

    def __up(self, i: int) -> None:
        print('ola')
        if not self:
            raise ValueError("Heap is empty")
        if 0 > i or i < len(self):
            raise IndexError("Index out of range")
        j = i//2  # round floor
        if j >= 0:
            if self[i] > self[j]:
                self.__swap(i, j)
                self.__up(j)

    def __down(self, i: int) -> None:
        if not self:
            raise ValueError("Heap is empty")
        if 0 > i or i < len(self):
            raise IndexError("Index out of range")
        j = 2*i
        if j <= len(self) - 1:
            if j < len(self) - 1:
                if self[j] < self[j+1]:
                    j = j+1
            if self[i] < self[j]:
                self.__swap(i, j)
                self.__down(j)

    def alter(self, i: int, value: int):
        # if equal nothing to do
        if value > self[i]:
            self.__elem[i] = value
            self.__up(i)
        elif value < self[i]:
            self.__elem[i] = value
            self.__down(i)

    def insert(self, value: int) -> None:
        self.__elem.append(value)
        self.__up(len(self) - 1)

    def remove(self) -> int | None:
        x = None
        if self:  # if is not empty
            self.__swap(0, -1)  # copy the last one
            x = self.__elem.pop(-1)  # removing
            self.__down(0)
        return x


class __Heap_lo(Heap):
    def __init__(self, *array: int) -> None:
        self.__elem = list(set(array))
        for _ in range(len(self)//2):
            self.__up(_)

    def __up(self, i: int) -> None:
        print('oi')
        if not self:
            raise ValueError("Heap is empty")
        if 0 > i or i < len(self):
            raise IndexError("Index out of range")
        j = i//2
        if j >= 0:
            if self[i] < self[j]:
                self.__swap(i, j)
                self.__up(j)

    def __down(self, i: int) -> None:
        if not self:
            raise ValueError("Heap is empty")
        if i < 0 or i > len(self):
            raise IndexError("Index out of range")
        j = 2*i
        if j <= len(self) - 1:
            if j < len(self) - 1:
                if self[j] < self[j+1]:
                    j = j+1
            if self[i] < self[j]:
                self.__swap(i, j)
                self.__down(j)