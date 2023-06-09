#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    tupla = ()
    a = tuple_a + (0, 0)
    b = tuple_b + (0, 0)
    tupla = a[0] + b[0], a[1] + b[1]
    return tupla
