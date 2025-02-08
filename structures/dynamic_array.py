"""
Skeleton for COMP3506/7505 A1, S2, 2024
The University of Queensland
Joel Mackenzie and Vladimir Morozov
"""

from typing import Any


class DynamicArray:
    def __init__(self) -> None:
        self._data = [None] * 5
        self._size = 0
        self._capacity = 5
        self._reverse = False
        self._start = self._capacity // 2

    def __str__(self) -> str:
        """
        A helper that allows you to print a DynamicArray type
        via the str() method.
        """
        for i in range(self._size):
            print(str(self.__getitem__(i)), end=" ")

    def __resize(self) -> None:
        self._capacity *= 2
        new_list = [None] * self._capacity
        for i in range(self._size):
            new_list[self._capacity // 2 - self._size // 2 + i] = self.__getitem__(i)
        self._start = self._capacity // 2 - self._size // 2
        self._data = new_list

    def get_at(self, index: int) -> Any | None:
        """
        Get element at the given index.
        Return None if index is out of bounds.
        Time complexity for full marks: O(1)
        """
        if self._size == 0 or index < 0 or index > self._size - 1:
            return None
        if self._reverse:
            index = self._size - index - 1
        return self._data[self._start + index]

    def __getitem__(self, index: int) -> Any | None:
        """
        Same as get_at.
        Allows to use square brackets to index elements.
        """
        return self.get_at(index)

    def set_at(self, index: int, element: Any) -> None:
        """
        Set element at the given index.
        Do not modify the list if the index is out of bounds.
        Time complexity for full marks: O(1)
        """
        if self._size == 0 or index < 0 or index > self._size - 1:
            return
        if self._reverse:
            index = self._size - index - 1
        self._data[self._start + index] = element

    def __setitem__(self, index: int, element: Any) -> None:
        """
        Same as set_at.
        Allows to use square brackets to index elements.
        """
        self.set_at(index, element)

    def append(self, element: Any) -> None:
        """
        Add an element to the back of the array.
        Time complexity for full marks: O(1*) (* means amortized)
        """
        if self._size + self._start == self._capacity or self._start == 0:
            self.__resize()
        if self._reverse:
            self._data[self._start - 1] = element
            self._start -= 1
        else:    
            self._data[self._start + self._size] = element
        self._size += 1

    def prepend(self, element: Any) -> None:
        """
        Add an element to the front of the array.
        Time complexity for full marks: O(1*)
        """
        if self._size + self._start == self._capacity or self._start == 0:
            self.__resize()
        if self._reverse:
            self._data[self._start + self._size] = element
        else:
            self._data[self._start - 1] = element
            self._start -= 1
        self._size += 1

    def reverse(self) -> None:
        """
        Reverse the array.
        Time complexity for full marks: O(1)
        """
        self._reverse = not self._reverse

    def remove(self, element: Any) -> None:
        """
        Remove the first occurrence of the element from the array.
        If there is no such element, leave the array unchanged.
        Time complexity for full marks: O(N)
        """
        for i in range(self._size):
            if self.__getitem__(i) == element:
                self.remove_at(i)
                return

    def remove_at(self, index: int) -> Any | None:
        """
        Remove the element at the given index from the array and return the removed element.
        If there is no such element, leave the array unchanged and return None.
        Time complexity for full marks: O(N)
        """
        if self._size == 0 or index < 0 or index > self._size - 1:
            return None
        elem = self._data.__getitem__(self._start + index)
        if self._reverse:
            index = self._size - index - 1

        for i in range(index, self._size - 1):
            self._data[self._start + i] = self._data[self._start + i + 1]
        self._data[self._start + self._size - 1] = None
        self._size -= 1
        return elem

    def is_empty(self) -> bool:
        """
        Boolean helper to tell us if the structure is empty or not
        Time complexity for full marks: O(1)
        """
        if self._size == 0:
            return True
        return False

    def is_full(self) -> bool:
        """
        Boolean helper to tell us if the structure is full or not
        Time complexity for full marks: O(1)
        """
        if self._size == self._capacity:
            return True
        return False

    def get_size(self) -> int:
        """
        Return the number of elements in the list
        Time complexity for full marks: O(1)
        """
        return self._size

    def get_capacity(self) -> int:
        """
        Return the total capacity (the number of slots) of the list
        Time complexity for full marks: O(1)
        """
        return self._capacity

    def sort(self) -> None:
        """
        Sort elements inside _data based on < comparisons.
        Time complexity for full marks: O(NlogN)
        """
        # merge sort
        if self._size <= 1:
            return self._data
        
        if self._size > 1:
            self.branch_out(0, self._size - 1)


    def branch_out(self, left: int, right: int) -> None:
        if left < right:
            mid = (left + right) // 2
            self.branch_out(left, mid)
            self.branch_out(mid + 1, right)
            self._merge(left, mid, right)
    
    def _merge(self, left: int, mid: int, right: int) -> None:
        left_size = mid - left + 1
        right_size = right - mid

        left_half = [None] * left_size
        right_half = [None] * right_size

        for i in range(left_size):
            left_half[i] = self.__getitem__(left + i)
        for j in range(right_size):
            right_half[j] = self.__getitem__(mid + 1 + j)

        L = 0 
        R = 0  
        M = left 

        # Merge the tempo arrays back
        while L < left_size and R < right_size:
            if left_half[L] <= right_half[R]:
                self.set_at(M, left_half[L])
                L += 1
            else:
                self.set_at(M, right_half[R])
                R += 1
            M += 1

        # remaining elements clean up
        while L < left_size:
            self.set_at(M, left_half[L])
            L += 1
            M += 1
        while R < right_size:
            self.set_at(M, right_half[R])
            R += 1
            M += 1