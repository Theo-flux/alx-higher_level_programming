#!/usr/bin/python3

'''Define a square class'''

class Square:
    '''Representation of a square'''

    def __init__(self, size=0):
        '''Instatiation'''
        self.size = size

    @property
    def size(self):
        '''Property: to retrieve data.

        Returns:
            To return data
        '''
        return self.__size

    @size.setter
    def size(self, value):
        '''property setter: to set it

        Args:
            value (int): value for data
        '''
        if (value < 0):
            raise ValueError('size must be >= 0')
        elif (not isinstance(value, int)):
            return TypeError('size must be a number')
        self.__size = value

    def area(self):
        '''Public instance method

        Returns:
            Area of current square
        '''
        return self.__size**2

    def __et__(self, other):
        '''equality comparator.

        Args:
            other (Square): instance of Square Type.
        '''
        return self.area() == other.area()

    def __ne__(self, other):
        '''not equal comparator

        Args:
            other (Square): instance of Square Type.
        '''
        return self.area() != other.area()

    def __gt__(self, other):
        '''greater than comparator

        Args:
            other (Square): instance of Square Type.
        '''
        return self.area() > other.area()

    def __ge__(self, other):
        '''greater than or equal comparator

        Args:
            other (Square): instance of Square Type.
        '''
        return self.area() >= other.area()

    def __lt__(self, other):
        '''less than comparator

        Args:
            other (Square): instance of Square Type.
        '''
        return self.area() < other.area()

    def __le__(self, other):
        '''less than comparator

        Args:
            other (Square): instance of Square Type.
        '''
        return self.area() <= other.area()
