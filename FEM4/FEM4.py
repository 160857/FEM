import numpy as np
import matplotlib  as plt

# wezly = np.array([[1, 0],
#                   [2, 1],
#                   [3, 0.5],
#                   [4, 0.75]])

# elementy = np.array([[1, 1, 3],
#                      [2, 4, 2],
#                      [4, 3, 4]])

# twb_L = 'D'
# twb_R = 'D'

# wwb_L = 0
# wwb_R = 1

def parametry_kontrolne(c, f):
    return c,f

def parametry_wstaw(sekcja, warunki, typy): 
    parametry = list(sekcja, warunki, typy)
    
    return  parametry

def geo_definicja(sekcja, wezly, c, f):
    x= sekcja[1] - sekcja[0]
    wezly_num = len(wezly)
    ilosc_elem = wezly_num - 1
    dlugosc_elem = x/ilosc_elem
    return x, wezly_num, ilosc_elem, dlugosc_elem

def Generuj(x_0,x_p,n):
    tmp = (x_p - x_0)/(n-1);
    przestrzen=np.array([x_0])
    i = []
    for i in range (1,n,1):
        przestrzen = np.block([przestrzen, i * tmp + x_0])
    return przestrzen
        
