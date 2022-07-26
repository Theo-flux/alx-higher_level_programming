#!/usr/bin/python3
"""
The ``100-matrix_mul`` module file
"""

def matrix_mul(m_a, m_b):
    """Function that multiplies 2 matrices.
    Args:
        m_a ([[]]): first matrix
        m_b ([[]]): second matrix
    Returns:
        a new matrix
    """
    if type(m_a) is not list:
        raise TypeError("m_a must be a list")

    if type(m_b) is not list:
        raise TypeError("m_b must be a list")

    if False in [False if type(row) != list else True for row in m_a]:
        raise TypeError("m_a must be a list of lists")

    if False in [False if type(row) != list else True for row in m_b]:
        raise TypeError("m_b must be a list of lists")
    
    if False in [False if type(col) not in [int, float] else True for row in m_a for col in row]:
        raise TypeError("m_a should contain only integers or floats")

    if [False in [False if type(col) not in [int, float] else True for row in m_b for col in row]:]:
        raise TypeError("m_b should contain only integers or floats")

    if max([len(row) for row in m_a]) != min([len(row) for row in m_a]):
        raise TypeError("each row of m_a must be of the same size")

    if max([len(row) for row in m_b]) != min([len(row) for row in m_b]):
        raise TypeError("each row of m_b must be of the same size")

    numOfRow_m_a = len(m_a[0])
    numOfCol_m_a = len(m_a)

    numOfRow_m_b = len(m_b[0])
    numOfCol_m_b = len(m_b)
