"""
Skeleton for COMP3506/7505 A1, S2, 2024
The University of Queensland
Joel Mackenzie and Vladimir Morozov
"""

# so we can hint Node get_next
from __future__ import annotations

from typing import Any


class Node:
    """
    A simple type to hold data and a next pointer
    """

    def __init__(self, data: Any) -> None:
        self._data = data  # This is the payload data of the node
        self._next = None  # This is the "next" pointer to the next Node
        self._prev = None  # This is the "previous" pointer to the previous Node

    def set_data(self, data: Any) -> None:
        self._data = data

    def get_data(self) -> Any:
        return self._data

    def set_next(self, node: Node) -> None:
        self._next = node

    def get_next(self) -> Node | None:
        return self._next

    def set_prev(self, node: Node) -> None:
        self._prev = node

    def get_prev(self) -> Node | None:
        return self._prev


class DoublyLinkedList:
    """
    Your doubly linked list code goes here.
    Note that any time you see `Any` in the type annotations,
    this refers to the "data" stored inside a Node.

    [V3: Note that this API was changed in the V3 spec] 
    """

    def __init__(self) -> None:
        # You probably need to track some data here...
        self._head = None
        self._tail = None
        self._size = 0
        self._reversed = False

    def __str__(self) -> str:
        """
        A helper that allows you to print a DoublyLinkedList type
        via the str() method.
        """
        pass

    """
    Simple Getters and Setters below
    """

    def get_size(self) -> int:
        """
        Return the size of the list.
        Time complexity for full marks: O(1)
        """
        return self._size

    def get_head(self) -> Any | None:
        """
        Return the data of the leftmost node in the list, if it exists.
        Time complexity for full marks: O(1)
        """
        return self._head.get_data() if self._head is not None else None

    def set_head(self, data: Any) -> None:
        """
        Replace the leftmost node's data with the given data.
        If the list is empty, do nothing.
        Time complexity for full marks: O(1)
        """
        if self._size == 0:
            return None
        self._head.set_data(data) if self._head is not None else None

    def get_tail(self) -> Any | None:
        """
        Return the data of the rightmost node in the list, if it exists.
        Time complexity for full marks: O(1)
        """
        return self._tail.get_data() if self._tail is not None else None

    def set_tail(self, data: Any) -> None:
        """
        Replace the rightmost node's data with the given data.
        If the list is empty, do nothing.
        Time complexity for full marks: O(1)
        """
        if self._size == 0:
            return None
        self._tail.set_data(data) if self._tail is not None else None

    """
    More interesting functionality now.
    """

    def insert_to_front(self, data: Any) -> None:
        """
        Insert the given data to the front of the list.
        Hint: You will need to create a Node type containing
        the given data.
        Time complexity for full marks: O(1)
        """
        new_data = Node(data)  
        if self._size == 0:
            self._head = new_data
            self._tail = new_data
            self._size += 1
            return
        self._head.set_prev(new_data)
        new_data.set_next(self._head)
        self._head = new_data
        self._size += 1

    def insert_to_back(self, data: Any) -> None:
        """
        Insert the given data (in a node) to the back of the list
        Time complexity for full marks: O(1)
        """
        new_data = Node(data)
        if self._size == 0:
            self._head = new_data
            self._tail = new_data
            self._size += 1
            return
        self._tail.set_next(new_data)
        new_data.set_prev(self._tail)
        self._tail = new_data
        self._size += 1

    def remove_from_front(self) -> Any | None:
        """
        Remove the front node, and return the data it holds.
        Time complexity for full marks: O(1)
        """
        if self._size == 0:
            return None
        data = self._head.get_data()
        if self._size == 1:
            self._head = None
            self._tail = None
            self._size -= 1
            return data
        self._head = self._head.get_next()
        self._head.set_prev(None)
        self._size -= 1
        return data

    def remove_from_back(self) -> Any | None:
        """
        Remove the back node, and return the data it holds.
        Time complexity for full marks: O(1)
        """
        if self._size == 0:
            return None
        data = self._tail.get_data()
        if self._size == 1:
            self._head = None
            self._tail = None
            self._size -= 1
            return data
        self._tail = self._tail.get_prev()
        self._tail.set_next(None)
        self._size -= 1
        return data

    def find_element(self, elem: Any) -> bool:
        """
        Looks at the data inside each node of the list and returns True
        if a match is found; False otherwise.
        Time complexity for full marks: O(N)
        """
        curr = self._head
        while curr is not None:
            if curr.get_data() == elem:
                return True
            curr = curr.get_next()
        return False

    def find_and_remove_element(self, elem: Any) -> bool:
        """
        Looks at the data inside each node of the list; if a match is
        found, this node is removed from the linked list, and True is returned.
        False is returned if no match is found.
        Time complexity for full marks: O(N)
        """
        curr = self._head
        while curr is not None:
            if curr.get_data() == elem:
                if curr.get_prev() is not None:
                    curr.get_prev().set_next(curr.get_next())
                if curr.get_next() is not None:
                    curr.get_next().set_prev(curr.get_prev())
                if curr == self._head:
                    self._head = curr.get_next()
                if curr == self._tail:
                    self._tail = curr.get_prev()
                self._size -= 1
                return True
            curr = curr.get_next()
        return False

    def reverse(self) -> None:
        """
        Reverses the linked list
        Time complexity for full marks: O(1)
        """
        self._reversed = not self._reversed
        self._head, self._tail = self._tail, self._head
