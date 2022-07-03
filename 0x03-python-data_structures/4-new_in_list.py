#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    copie = [i for i in my_list]
    if idx < 0 or idx > len(copie) - 1:
        return copie
    copie[idx] = element
    return copie
