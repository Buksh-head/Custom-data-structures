"""
Skeleton for COMP3506/7505 A1, S2, 2024
The University of Queensland
Joel Mackenzie and Vladimir Morozov
"""

from typing import Any

from structures.dynamic_array import DynamicArray


class BitVector:
    """
    A compact storage for bits that uses DynamicArray under the hood.
    Each element stores up to 64 bits, making BitVector 64 times more memory-efficient
    for storing bits than plain DynamicArray.
    """

    BITS_PER_ELEMENT = 64

    def __init__(self) -> None:
        """
        We will use the dynamic array as our data storage mechanism
        """
        self._data = DynamicArray()
        # you may want or need more stuff here in the constructor
        self._data.append(0)
        self._data.append(0)
        self._size = 0
        self._capacity = 2
        self._reverse = False
        self._flipped = False

    def __str__(self) -> str:
        """
        A helper that allows you to print a BitVector type
        via the str() method.
        """
        loop = self._size // self.BITS_PER_ELEMENT + 1
        for i in range(loop):
            if self._reverse:
                print(bin(self._data.get_at(i)), end=" ")
            else:
                print(bin(self._data.get_at(i)), end=" ")

    def __resize(self) -> None:
        # note not right
        self._capacity *= 2   
        new_data = DynamicArray()
        for _ in range(self._capacity):
            new_data.append(0)
        # Copy the old data into the new array
        for i in range(self._capacity // 2):
            new_data.set_at(i, self._data.get_at(i))

        self._data = new_data

    def get_at(self, index: int) -> int | None:
        """
        Get bit at the given index.
        Return None if index is out of bounds.
        Time complexity for full marks: O(1)
        """
        if index < 0 or index > self._size - 1:
            return None
        if self._reverse:
            index = self._size - index - 1
        
        element_pos = index // self.BITS_PER_ELEMENT
        bit_pos = index % self.BITS_PER_ELEMENT
        
        if self._flipped:
            return (self._data.get_at(element_pos) >> bit_pos) & 1 ^ 1 #XOR
        return (self._data.get_at(element_pos) >> bit_pos) & 1

    def __getitem__(self, index: int) -> int | None:
        """
        Same as get_at.
        Allows to use square brackets to index elements.
        """
        return self.get_at(index)

    def set_at(self, index: int) -> None:
        """
        Set bit at the given index to 1.
        Do not modify the vector if the index is out of bounds.
        Time complexity for full marks: O(1)
        """
        if index < 0 or index > self._size:
            return
        if self._reverse:
            index = self._size - index - 1

        element_pos = index // self.BITS_PER_ELEMENT 
        bit_pos = index % self.BITS_PER_ELEMENT

        if self._flipped:
            self._data[element_pos] &= ~(1 << bit_pos)
            return
        self._data[element_pos] |= (1 << bit_pos)

    def unset_at(self, index: int) -> None:
        """
        Set bit at the given index to 0.
        Do not modify the vector if the index is out of bounds.
        Time complexity for full marks: O(1)
        """
        if index < 0 or index >= self._capacity * self.BITS_PER_ELEMENT:
            return
        if self._reverse:
            index = self._size - index - 1
        if self._size <= index:
            self._size = index + 1
        
        element_pos = index // self.BITS_PER_ELEMENT
        bit_pos = index % self.BITS_PER_ELEMENT

        if self._flipped:
            self._data[element_pos] |= (1 << bit_pos)
            return
        
        self._data[element_pos] &= ~(1 << bit_pos)

    def __setitem__(self, index: int, state: int) -> None:
        """
        Set bit at the given index.
        Treat the integer in the same way Python does:
        if state is 0, set the bit to 0, otherwise set the bit to 1.
        Do not modify the vector if the index is out of bounds.
        Time complexity for full marks: O(1)
        """
        self.set_at(index) if state else self.unset_at(index)

    def append(self, state: int) -> None:
        """
        Add a bit to the back of the vector.
        Treat the integer in the same way Python does:
        if state is 0, set the bit to 0, otherwise set the bit to 1.
        Time complexity for full marks: O(1*)
        """
        if self._size == self._capacity * self.BITS_PER_ELEMENT:
            self.__resize()

        if self._flipped:
            state = not state

        if self._reverse:
            if self._size < self.BITS_PER_ELEMENT:
                self._data[0] <<= 1
                self._data[0] ^= state
            for i in range(self._size // self.BITS_PER_ELEMENT, 0, -1):
                end = self._data[i] >> self._size - 1
                self._data[i] <<= 1
                if i == 0:
                    self._data[i] ^= state
                else:
                    self._data[i] ^= end
  
        else:    
            element_pos = self._size // self.BITS_PER_ELEMENT
            bit_pos = self._size % self.BITS_PER_ELEMENT
            if state != 0:
                self._data[element_pos] |= (1 << bit_pos)
        self._size += 1
        

    def prepend(self, state: Any) -> None:
        """
        Add a bit to the front of the vector.
        Treat the integer in the same way Python does:
        if state is 0, set the bit to 0, otherwise set the bit to 1.
        Time complexity for full marks: O(1*)
        """
        # note make better
        if self._size == self._capacity * self.BITS_PER_ELEMENT:
            self.__resize()

        if self._flipped:
            state = not state
            
        if self._reverse:
            element_pos = self._size // self.BITS_PER_ELEMENT
            bit_pos = self._size % self.BITS_PER_ELEMENT
            if state != 0:
                self._data[element_pos] |= (1 << bit_pos)
        else:
            if self._size < self.BITS_PER_ELEMENT:
                self._data[0] <<= 1
                self._data[0] ^= state
            for i in range(self._size // self.BITS_PER_ELEMENT, 0, -1):
                end = self._data[i] >> self._size - 1
                self._data[i] <<= 1
                if i == 0:
                    self._data[i] ^= state
                else:
                    self._data[i] ^= end

        self._size += 1

    def reverse(self) -> None:
        """
        Reverse the bit-vector.
        Time complexity for full marks: O(1)
        """
        self._reverse = not self._reverse

    def flip_all_bits(self) -> None:
        """
        Flip all bits in the vector.
        Time complexity for full marks: O(1)
        """
        self._flipped = not self._flipped

    def shift(self, dist: int) -> None:
        """
        Make a bit shift.
        If dist is positive, perform a left shift by `dist`.
        Otherwise perform a right shift by `dist`.
        Time complexity for full marks: O(N)
        """
        if dist == 0:
            return
        for i in range(self._size // self.BITS_PER_ELEMENT + 1):
            if dist > 0:
                self._data[i] <<= dist  
            if dist < 0:
                self._data[i] >>= -dist            

    def rotate(self, dist: int) -> None:
        """
        Make a bit rotation.
        If dist is positive, perform a left rotation by `dist`.
        Otherwise perform a right rotation by `dist`.
        Time complexity for full marks: O(N)
        """
        num = 0
        if dist == 0:
            return
        for i in range(abs(dist) % self._size):
            if dist > 0:
                if self._reverse:
                    if self._flipped:
                        num |= self.get_at(i) ^ 1
                    else:
                        num |= self.get_at(i)
                else:
                    if self._flipped:
                        num |= self.get_at(self._size - 1 - i) ^ 1
                    else:
                        num |= self.get_at(self._size - 1 - i)
            else:
                if self._reverse:
                    if self._flipped:
                        num |= self.get_at(self._size + dist + i) ^ 1
                    else:
                        num |= self.get_at(self._size + dist + i)
                else:
                    if self._flipped:
                        num |= self.get_at(-dist - i - 1) ^ 1
                    else:
                        num |= self.get_at(-dist - i - 1)
            num <<= 1
        num >>= 1
                
        for j in range(self._size // self.BITS_PER_ELEMENT + 1):
            if dist > 0:
                self._data[j] <<= dist  
            if dist < 0:
                self._data[j] >>= -dist
        if dist < 0:
            self._data[self._size // self.BITS_PER_ELEMENT] |= num << self._size % self.BITS_PER_ELEMENT + dist
        else:
            self._data[0] |= num
        

    def get_size(self) -> int:
        """
        Return the number of *bits* in the list
        Time complexity for full marks: O(1)
        """
        return self._size
    
    def increase_capacity(self) -> None:
        self._capacity *= 2
        new_data = DynamicArray()
        for _ in range(self._capacity):
            new_data.append(0)
        for i in range(self._capacity // 2):
            new_data.set_at(i, self._data.get_at(i))

        self._data = new_data
        self._size = self._capacity * self.BITS_PER_ELEMENT

    def expand_capacity(self) -> None:
        #self.BITS_PER_ELEMENT = 2 ** 32
        self._capacity *= 2 ** 25   
        new_data = DynamicArray(init_data=[0] * self._capacity, init_size=self._capacity)
        self._data = new_data
        self._size = self._capacity * self.BITS_PER_ELEMENT
    
    def get_capacity(self) -> int:
        return self._capacity   
