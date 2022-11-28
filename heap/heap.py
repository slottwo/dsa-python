class Heap():
    def __init__(self, *vector: int) -> None:
        self._elem = list(vector)
        for i in range(len(vector)//2, 0, -1):
            self.__down(i)

    def __up(self, i: int):
        j = i//2  # round floor
        if j >= 0:
            if self._elem[i] > self._elem[j]:
                self._elem[i], self._elem[j] = self._elem[j], self._elem[i]
                self.__up(j)

    def __down(self, i: int):
        j = 2*i
        if j <= len(self._elem) - 1:
            if j < len(self._elem) - 1:
                if self._elem[j] < self._elem[j+1]:
                    j = j+1
            if self._elem[i] < self._elem[j]:
                self._elem[i], self._elem[j] = self._elem[j], self._elem[i]
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
        n = len(self._elem)
        self.__up(n-1)

    def remove(self):
        self._elem[0] = self._elem[-1]  # copy the last one
        self._elem.pop(-1)  # remove it
        self.__down(0)

    def Heapsort(self):
        pass


h = Heap(2, 3, 404, 29, 0, 12)
print(h._elem)
