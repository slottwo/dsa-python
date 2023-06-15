class HashTable:
    def __init__(self, size: int, *elements: any) -> None:
        """Create a hash table object with external collisions.

        Args:
            size (int): _description_
            elements (Any): _description_

        Raises:
            ValueError: If the size is less than 1
        """

        if size <= 0:
            raise ValueError("Hash table size cannot be zero or lower.")

        self.__table: tuple[list] = tuple([] for i in range(size))

        self.__size = size

        for element in elements:
            self.insert(element)

    def __hash(self, __value): return hash(__value) % self.N

    @property
    def N(self) -> int:  # gets __size private attribute
        """The size of table, how many lines it has."""
        return self.__size

    @N.setter
    def N(self, __value: int):  # reformat with a new size
        items = []
        for li in self.__table:
            items += li
        self = HashTable(__value, *items)

    def __repr__(self) -> str:  # use for pretty prints
        s = 'Table:'
        for k, v in enumerate(self.__table):
            s += f'\n    {k}: {v}'
        return s

    def __len__(self) -> int:
        return sum(len(li) for li in self.__table)

    def __getitem__(self, __index: int) -> int:
        return self.__table[__index]

    def __contains__(self, __value: any):  # search
        i = self.__hash(__value)
        return __value in self.__table[i]

    def insert(self, __value: any):
        if __value not in self:
            i = self.__hash(__value)
            self.__table[i].append(__value)

    def remove(self, __value: any):
        if __value in self:
            i = self.__hash(__value)
            self.__table[i].remove(__value)


if __name__ == '__main__':
    # Testing
    def __test(n, to_in: tuple[int], to_re: tuple[int]):
        t = HashTable(n)

        # Total items check
        assert len(t) == 0

        # Size check
        assert t.N == n

        # Output check
        empty_out = 'Table:\n    ' + \
            '\n    '.join(f'{i}: []' for i in range(n))
        assert t.__repr__() == empty_out

        print(str(t).replace(':', ' after startup:', 1))

        # Insertion check
        for i in to_in:
            t.insert(i)
            assert i in t
            assert i in t[i % n]

        print(str(t).replace(':', ' after insertions:', 1))

        # Removal check
        for i in to_re:
            t.remove(i)
            assert i not in t
            assert i not in t[i % n]

        print(str(t).replace(':', ' after removals:', 1))

    try:
        HashTable(0)
    except ValueError:
        pass
    else:
        raise NotImplementedError('HashTable should not accept 0 as size')

    # Exemple
    __test(4, (1, 2, 3, 4), (3, 4, 5))
