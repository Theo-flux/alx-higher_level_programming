#!/usr/bin/python3

"""Define A Node Class"""


class Node:
    """A representation of a Node."""

    def __init__(self, data, next_node=None):
        """Instantiation with data and next_node."""
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Property: Private instance attribute:data."""
        return self.__data

    @data.setter
    def data(self, value):
        """Property setter: To set Private instance attribute: data.

        Args:
            value (int): integer value to set private attribute: data.
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Property: Private instance attribute: next_node."""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Property setter: Private instance attribute: next_node.

        Args:
            value (Node): Node value to set the private attribute: next_node.
        """
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value
    
"""Define A SinglyLinkedList Class"""

class SinglyLinkedList:
    """A representation of singlylinkedlist."""

    def __init__(self):
        """Simple instantiation."""
        self.__head = None

    def sorted_insert(self, value):
        """Public instance method that inserts a new Node
            into the correct sorted position in the list (increasing order)

        Args:
            value (Node): Node value to insert.
        """
        new = Node(value)
        if (self.__head == None):
            new.next_node = None
            self.__head = new
        elif (self.__head.data > value):
            new.next_node = self.__head
            self.__head = new
        else:
            tmp = self.__head
            while (tmp.next_node != None and tmp.next_node.data < value):
                tmp = tmp.next_node
            new.next_node = None
            tmp.next_node = new

    def __str__(self):
        """Print the entire list in stdout. one node number by line."""
        llist = []
        tmp = self.__head
        while tmp != None:
            llist.append(str(tmp.data))
            tmp = tmp.next_node
        return("\n".join(llist))
