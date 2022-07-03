#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    copie = my_list.copy()
    
    if idx < 0 or idx > len(my_list):
        return copie
    copie[idx] = element
    return copie
