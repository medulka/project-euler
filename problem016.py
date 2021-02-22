#!/usr/bin/env python3
"""
Project Euler
Problems 016
created on 08.02.2021
in: Kuri8
"""

#What is the sum of the digits of the number 21000?

def compute(n):
    lst = list(str(2**n))
    lst = [int(i) for i in lst]
    return sum(lst)


compute(4)    
compute(1000)

#bez pocitani s velkymi cisly

###dve na n-tou pomoci nasobeni seznamu cislic dvema
def nasobeni_dvema(a):
    "input:lst, output: kazdy clen seznamu vynasobeny dvema"
    for i in range(0,len(a)):
        a[i] = a[i]*2
    for i in range(1,len(a)):    
        if a[i-1] > 9:
            a[i] = a[i] + 1
    if a[-1] > 9: 
        a.append(1)
    for i in range(0, len(a)):
        a[i] = a[i] % 10
    return a

nasobeni_dvema([1])

def dve_na_ntou(n):
    "input: a natural number, output: the result"
    vysledek = [1]
    for x in range(1,n+1):
       vysledek = nasobeni_dvema(vysledek)
    vysledek = [str(el) for el in vysledek]
    vysledek = list(reversed(vysledek))   
    vysledek = int("".join(vysledek))       
    return vysledek

dve_na_ntou(5)
dve_na_ntou(1000)

###dve na n-tou pomoci scitani seznamu cislic dvema
def nasobeni_dvema(a):
    "input: a list, output: a list "
    vysledek = [(a[0] + a[0]) % 10]
    for i in range(1,len(a)):
        soucet = (a[i] + a[i]) % 10
        if a[i-1] + a[i-1] > 9:
            soucet += 1 
        vysledek.append(soucet)   
    if a[-1] + a[-1] > 9:s
        vysledek.append(1)    
    return vysledek

nasobeni_dvema([4,9])


def mocnina_dvou(n):
    "input: a natural number, output: the result"
    vysledek = [1]
    for x in range(1,n+1):
       vysledek = nasobeni_dvema(vysledek)
    vysledek = [str(el) for el in vysledek]
    vysledek = list(reversed(vysledek))   
    vysledek = int("".join(vysledek))       
    return vysledek

mocnina_dvou(5)

###funguje


###prepouzivani fci

from ProjectEuler import problem013




    