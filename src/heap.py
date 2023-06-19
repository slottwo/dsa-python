from typing import Iterator


class MinHeap:
    def __init__(H, *values) -> None:
        H.__elements = list(values)

    def __getitem__(H, __index: int) -> int:
        return H.__elements[__index-1]

    def __setitem__(H, __index: int, __value: float):
        H.__elements[__index-1] = __value

    def __iter__(H) -> Iterator:
        return iter(H.__elements)

    def __up(H, __index: int) -> bool:
        if __index > 1:
            __lower_idx = __index / 2
            if H[__lower_idx] > H[__index]:
                H[__lower_idx], H[__index] = H[__lower_idx], H[__index]
                H.__up(__lower_idx)
                return True
        return False

    def __down(H, __index: int) -> bool:
        __upper_idx = __index * 2
        if __upper_idx < len(H):
            if H[__upper_idx + 1] < H[__upper_idx]:
                __upper_idx += 1
            if H[__upper_idx] < H[__index]:
                H[__upper_idx], H[__index] = H[__upper_idx], H[__index]
                H.__down(__upper_idx)
                return True
        return False


H = MinHeap(1, 2, 3, 4)
H[0] = 5
print(*H)
