'''
https://www.programcreek.com/2015/03/rotate-array-in-java/

>>> rotate_array([1,2,3,4,5,6,7], 3)
[5, 6, 7, 1, 2, 3, 4]
'''

def rotate_array(k, n):
    primeira_fatia = k[: n + 1]
    segunda_fatia = k[4:]

    return segunda_fatia + primeira_fatia
