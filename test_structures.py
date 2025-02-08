"""
Skeleton for COMP3506/7505 A1, S2, 2024
The University of Queensland
Joel Mackenzie and Vladimir Morozov

NOTE: This file is not used for assessment. It is just a driver program for
you to write your own test cases and execute them against your data structures.
"""

# Import helper libraries
import random
import sys
import time
import argparse

# Import our data structures
from structures.linked_list import Node, DoublyLinkedList
from structures.dynamic_array import DynamicArray 
from structures.bit_vector import BitVector

def test_linked_list():
    """
    A simple set of tests for the linked list implementation.
    This is not marked and is just here for you to test your code.
    """
    print ("==== Executing Linked List Tests ====")

    # Consider expanding these tests into your own methods instead of
    # just doing a bunch of stuff here - this is just to get you started
    
    # OK, let's add some strings to a list
    my_list = DoublyLinkedList()
    assert(my_list.get_size() == 0)

    my_list.insert_to_front(Node("hello"))
    my_list.insert_to_back(Node("algorithms"))

    # Have a look - we can do this due to overriding __str__ in the class
    print(str(my_list))

    # Now lets try to find a node
    elem = my_list.find_element("algorithms")
    if elem is not None:
        print ("Found node with data = ", elem.get_data())

    # And try to delete one
    elem = my_list.find_and_remove_element("1337")
    if elem is not None:
        print ("Deleted ", elem.get_data())
    else:
        print ("Didn't find element = 1337")

    # And try to delete another one
    elem = my_list.find_and_remove_element("hello")
    if elem is not None:
        print ("Deleted ", elem.get_data())
    else:
        print ("Didn't find element = world")

    # Have another look
    print(str(my_list))

    # OK, now check size
    assert(my_list.get_size() == 1)

def test_dynamic_array():
    """
    A simple set of tests for the dynamic array implementation.
    This is not marked and is just here for you to test your code.
    """
    print ("==== Executing Dynamic Array Tests ====")
    # Initialize the DynamicArray
    arr = DynamicArray()

    # Test appending elements
    arr.append(1)
    arr.append(2)
    arr.append(3)
    print(arr.get_capacity())
    print(arr.get_size())
    print("0",arr.get_at(0))
    print(arr.get_at(1))
    print("2",arr.get_at(2))
    print(arr.get_at(3))
    print(arr.get_at(4))
    assert arr.get_size() == 3, "Size should be 3 after three appends"
    assert arr.get_at(0) == 1, "Element at index 0 should be 1"
    assert arr.get_at(1) == 2, "Element at index 1 should be 2"
    assert arr.get_at(2) == 3, "Element at index 2 should be 3"

    # Test prepending elements
    arr.prepend(0)
    assert arr.get_size() == 4, "Size should be 4 after one prepend"
    assert arr.get_at(0) == 0, "Element at index 0 should be 0"
    assert arr.get_at(1) == 1, "Element at index 1 should be 1"

    # Test reversing the array
    arr.reverse()
    print(arr.__str__())
    assert arr.get_at(0) == 3, "Element at index 0 should be 3 after reversing"
    assert arr.get_at(1) == 2, "Element at index 1 should be 2 after reversing"
    assert arr.get_at(2) == 1, "Element at index 2 should be 1 after reversing"
    assert arr.get_at(3) == 0, "Element at index 3 should be 0 after reversing"

    # Test re-reversing the array (back to original order)
    arr.reverse()
    assert arr.get_at(0) == 0, "Element at index 0 should be 0 after reversing again"
    assert arr.get_at(1) == 1, "Element at index 1 should be 1 after reversing again"
    assert arr.get_at(2) == 2, "Element at index 2 should be 2 after reversing again"
    assert arr.get_at(3) == 3, "Element at index 3 should be 3 after reversing again"

    # Test appending after reversing
    arr.reverse()
    arr.append(4)
    print(arr.__str__())
    assert arr.get_size() == 5, "Size should be 5 after append"
    assert arr.get_at(0) == 3, "Element at index 0 should be 3 after reverse and append"
    assert arr.get_at(4) == 4, "Element at index 4 should be 4 after reverse and append"

    # Test prepending after reversing back to original order
    arr.reverse()
    arr.prepend(-1)
    print(arr.__str__())
    assert arr.get_size() == 6, "Size should be 6 after prepend"
    assert arr.get_at(0) == -1, "Element at index 0 should be -1 after prepend"
    assert arr.get_at(2) == 0, "Element at index 1 should be 0 after prepend"

    # Test get_at with out of bounds indices
    assert arr.get_at(-1) is None, "Negative index should return None"
    assert arr.get_at(10) is None, "Index out of bounds should return None"

    # Test remove and remove_at
    arr.remove(2)
    assert arr.get_size() == 5, "Size should be 5 after removing element 2"
    assert arr.get_at(2) != 2, "Element 2 should not be in the array after removal"

    removed_elem = arr.remove_at(2)
    assert removed_elem == 0, "Removed element should be 0"
    assert arr.get_size() == 4, "Size should be 4 after removing at index 1"
    assert arr.get_at(1) != 0, "Element 0 should not be in the array after removal"

    # Final array should be [-1, 1, 3, 4]
    expected_final = [-1, 4, 1, 3]
    for i in range(arr.get_size()):
        assert arr.get_at(i) == expected_final[i], f"Element at index {i} should be {expected_final[i]}"
    print("All tests passed!")
    # Initialize the DynamicArray
    arr = DynamicArray()

    # Test reversing and then appending enough elements to trigger resizing
    arr.append(1)
    arr.append(2)
    arr.append(3)
    arr.append(4)
    arr.append(5)  # This should fill the initial capacity
    assert arr.get_size() == 5, "Size should be 5 after five appends"

    arr.reverse()  # Reverse the array
    arr.append(6)  # This should trigger a resize

    assert arr.get_size() == 6, "Size should be 6 after appending an element to a reversed array"
    assert arr.get_capacity() > 5, "Capacity should have increased after resizing"

    # Check the order after reversing and resizing
    expected = [5, 4, 3, 2, 1, 6]
    for i in range(arr.get_size()):
        assert arr.get_at(i) == expected[i], f"Element at index {i} should be {expected[i]} after reverse and resize"

    # Test reversing again and prepending elements
    arr.reverse()  # Reverse back to original order
    print(arr.__str__())
    arr.prepend(0)
    print(arr.__str__())
    arr.prepend(-1)  # This should trigger another resize
    print(arr.__str__())

    assert arr.get_size() == 8, "Size should be 8 after prepending two elements"
    assert arr.get_capacity() > 5, "Capacity should have increased again after resizing"

    # Check the order after reversing, resizing, and prepending
    expected = [-1, 0, 6, 1, 2, 3, 4, 5]
    for i in range(arr.get_size()):
        assert arr.get_at(i) == expected[i], f"Element at index {i} should be {expected[i]} after reverse, resize, and prepend"

    # Further tests: removing elements after resizing and reversing
    arr.remove(3)  # Remove element 3
    assert arr.get_size() == 7, "Size should be 7 after removing element 3"
    assert arr.get_at(3) == 1, "Element at index 3 should be 4 after removing element 3"

    arr.reverse()  # Reverse the array again
    arr.remove_at(0)  # Remove the first element in the reversed order

    assert arr.get_size() == 6, "Size should be 6 after removing the first element in reversed order"
    assert arr.get_at(0) == 4, "Element at index 0 should be 6 after removing the first element in reversed order"
    
    print(arr.__str__())
    arr.sort()  # Sort the array
    print(arr.get_size())
    print(arr.__str__())
    arr.remove_at(2)  # Remove the first element after sorting
    print(arr.__str__())
    arr.remove(4)
    print(arr.__str__())
    arr.remove(50)
    print(arr.__str__())
    arr.remove_at(10)
    print(arr.__str__())
    arr.prepend(0)
    print(arr.__str__())
    arr.append(0)
    print(arr.__str__())
    arr.remove_at(0)
    print(arr.__str__())
    print(arr.get_size())
    arr.remove_at(0)
    print(arr.get_size())
    arr.remove_at(0)
    print(arr.get_size())
    arr.remove_at(0)
    print(arr.get_size())
    arr.remove_at(0)
    print(arr.get_size())
    print(arr.__str__())
    arr.remove_at(0)
    print(arr.get_size())
    print(arr.__str__())


def test_bitvector():
    """
    A simple set of tests for the bit vector implementation.
    This is not marked and is just here for you to test your code.
    """
    print ("==== Executing Bit Vector Tests ====")



# The actual program we're running here
if __name__ == "__main__":
    # Get and parse the command line arguments
    parser = argparse.ArgumentParser(description="COMP3506/7505 Assignment One: Testing Data Structures")

    parser.add_argument("--linkedlist", action="store_true", help="Test your linked list.")
    parser.add_argument("--dynamicarray", action="store_true", help="Test your dynamic array.")
    parser.add_argument("--bitvector", action="store_true", help="Test your bit vector.")
    parser.add_argument("--seed", type=int, default='42', help="Seed the PRNG.")
    
    args = parser.parse_args()

    # No arguments passed
    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit(-1)

    # Seed the PRNG in case you are using randomness
    random.seed(args.seed)

    # Now check/run the selected algorithm
    if args.linkedlist:
        test_linked_list()

    if args.dynamicarray:
        test_dynamic_array()

    if args.bitvector:
        test_bitvector()

