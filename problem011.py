
#!/usr/bin/env python3

"""
Project Euler
Problems 011
created on 21.01.2021

"""

#011 What is the greatest product of four adjacent numbers in the same direction (up, down, left, right, or diagonally) in the 20×20 grid?

raw_grid = '''
08 02 22 97 38 15 00 40 00 75 04 05 07 78 52 12 50 77 91 08
49 49 99 40 17 81 18 57 60 87 17 40 98 43 69 48 04 56 62 00
81 49 31 73 55 79 14 29 93 71 40 67 53 88 30 03 49 13 36 65
52 70 95 23 04 60 11 42 69 24 68 56 01 32 56 71 37 02 36 91
22 31 16 71 51 67 63 89 41 92 36 54 22 40 40 28 66 33 13 80
24 47 32 60 99 03 45 02 44 75 33 53 78 36 84 20 35 17 12 50
32 98 81 28 64 23 67 10 26 38 40 67 59 54 70 66 18 38 64 70
67 26 20 68 02 62 12 20 95 63 94 39 63 08 40 91 66 49 94 21
24 55 58 05 66 73 99 26 97 17 78 78 96 83 14 88 34 89 63 72
21 36 23 09 75 00 76 44 20 45 35 14 00 61 33 97 34 31 33 95
78 17 53 28 22 75 31 67 15 94 03 80 04 62 16 14 09 53 56 92
16 39 05 42 96 35 31 47 55 58 88 24 00 17 54 24 36 29 85 57
86 56 00 48 35 71 89 07 05 44 44 37 44 60 21 58 51 54 17 58
19 80 81 68 05 94 47 69 28 73 92 13 86 52 17 77 04 89 55 40
04 52 08 83 97 35 99 16 07 97 57 32 16 26 26 79 33 27 98 66
88 36 68 87 57 62 20 72 03 46 33 67 46 55 12 32 63 93 53 69
04 42 16 73 38 25 39 11 24 94 72 18 08 46 29 32 40 62 76 36
20 69 36 41 72 30 23 88 34 62 99 69 82 67 59 85 74 04 36 16
20 73 35 29 78 31 90 01 74 31 49 71 48 86 81 16 23 57 05 54
01 70 54 71 83 51 54 69 16 92 33 48 61 43 52 01 89 19 67 48
'''

###the list in the list - Spiegel im Spiegel

def str_to_list(retezec):
    "in: vnitrni string, out: list(int)"
    slova = retezec.split(' ')
    return [int(slovo) for slovo in slova]
   
def data_preprocessing(raw_grid):
    "Dovnitr: str, Vrati: list(list(int))"
    radky = raw_grid.strip().split('\n') #f(1)
    return [str_to_list(radka) for radka in radky] 

def nej_soucin_radek_f(grid):
    return max([grid[i][l] * grid[i][l+1] * grid[i][l+2] * grid[i][l+3] for i in range(0, 20) for l in range(0,16)])

def nej_soucin_sloupec_f(grid):
    return max([grid[i][l] * grid[i+1][l] * grid[i+2][l] * grid[i+3][l] for i in range(0, 16) for l in range(0,20)])

def nej_soucin_diagonalne_f(grid):
    return max([grid[i][l] * grid[i+1][l+1] * grid[i+2][l+2] * grid[i+3][l+3] for i in range(0, 16) for l in range(0,16)])

def nej_soucin_diagonalne_zpetne_f(grid):
    return max([grid[i][l] * grid[i+1][l-1] * grid[i+2][l-2] * grid[i+3][l-3] for i in range(0, 16) for l in range(3,20)])

def highest_grid_product(grid):
    return max([nej_soucin_radek_f(grid), nej_soucin_sloupec_f(grid), nej_soucin_diagonalne_f(grid), nej_soucin_diagonalne_zpetne_f(grid) ])

processed_grid = data_preprocessing(raw_grid)
print(highest_grid_product(processed_grid))  


nej_soucin_diagonalne_zpetne_f(processed_grid)



###############
#notes

'''
raw_grid = '''
08 02 22 97 38 15 00 40 00 75 04 05 07 78 52 12 50 77 91 08
49 49 99 40 17 81 18 57 60 87 17 40 98 43 69 48 04 56 62 00
81 49 31 73 55 79 14 29 93 71 40 67 53 88 30 03 49 13 36 65
52 70 95 23 04 60 11 42 69 24 68 56 01 32 56 71 37 02 36 91
22 31 16 71 51 67 63 89 41 92 36 54 22 40 40 28 66 33 13 80
24 47 32 60 99 03 45 02 44 75 33 53 78 36 84 20 35 17 12 50
32 98 81 28 64 23 67 10 26 38 40 67 59 54 70 66 18 38 64 70
67 26 20 68 02 62 12 20 95 63 94 39 63 08 40 91 66 49 94 21
24 55 58 05 66 73 99 26 97 17 78 78 96 83 14 88 34 89 63 72
21 36 23 09 75 00 76 44 20 45 35 14 00 61 33 97 34 31 33 95
78 17 53 28 22 75 31 67 15 94 03 80 04 62 16 14 09 53 56 92
16 39 05 42 96 35 31 47 55 58 88 24 00 17 54 24 36 29 85 57
86 56 00 48 35 71 89 07 05 44 44 37 44 60 21 58 51 54 17 58
19 80 81 68 05 94 47 69 28 73 92 13 86 52 17 77 04 89 55 40
04 52 08 83 97 35 99 16 07 97 57 32 16 26 26 79 33 27 98 66
88 36 68 87 57 62 20 72 03 46 33 67 46 55 12 32 63 93 53 69
04 42 16 73 38 25 39 11 24 94 72 18 08 46 29 32 40 62 76 36
20 69 36 41 72 30 23 88 34 62 99 69 82 67 59 85 74 04 36 16
20 73 35 29 78 31 90 01 74 31 49 71 48 86 81 16 23 57 05 54
01 70 54 71 83 51 54 69 16 92 33 48 61 43 52 01 89 19 67 48
'''

first_row = '''
08 02 22 97 38 15 00 40 00 75 04 05 07 78 52 12 50 77 91 08
'''


grid = grid.replace('\n', ' ').split(' ')
grid = [int(i) for i in grid[1:-1]]
first_row = first_row.replace('\n', ' ').split(' ')
#first_row = [int(i) for i in first_row[1:-1]]
step = len(first_row)  #20

grid[(len(first_row)*r +c]




def row_product():  #34,345,080
    max_product = 0
    #NUMBER = 0 ???
    #PRODUCT = 0       
    for number in grid:  
        product = grid[number] * grid[number + 1] * grid[number + 2] * grid[number + 3]
        if product > max_product:
            max_product = product  #NE ==
        number += 1                # grid[number] += 1 ???
    return max_product

def column_product():  #32,551,430
    max_product = 0
    for number in grid:
        product = grid[number] * grid[number + 20] * grid[number + 40] * grid[number + 60]
        #print(grid[number], number, product)   #sort ???
        if product > max_product:
            max_product = product  
        number += 1                

def diagonal_product():  #44,793,000
    max_product = 0
    for number in grid:
        product = grid[number] * grid[number + 21] * grid[number + 42] * grid[number + 63]
        #print(grid[number], number, product)   #sort ???
        if product > max_product:
            max_product = product  
        number += 1                
    return max_product

def highest_grid_product():
    return max(row_product(), column_product(), diagonal_product())
     
highest_grid_product()



# web scrapping - urllib

import urllib.request
with urllib.request.urlopen('https://projecteuler.net/problem=11') as f:
    if f.status != 200:
        raise Exception('Failed to download')
    data = f.read().decode('utf-8')
    
print(data)
#nefungovala knihovna lxml

# web scrapping - BeautifulSoup
from bs4 import BeautifulSoup
soup = BeautifulSoup(data)

for p in soup.find_all('p'):
    if p.attrs != {'class': ['monospace', 'center']}:
        continue
    grid_str = p.get_text().strip()
    break
grid = [int(i) for i in grid_str.split()]
print(grid)
assert grid_str   
print(repr(grid))


###the list in the list - Spiegel im Spiegel

def str_to_list(retezec):
    "in: vnitrni string, out: list(int)"
    slova = retezec.split(' ')
    return [int(slovo) for slovo in slova]
   

 def data_preprocessing(raw_grid):
    "Dovnitr: str, Vrati: list(list(int))"
    radky = raw_grid.strip().split('\n') #f(1)
    return [str_to_list(radka) for radka in radky] 
    

processed_grid = data_preprocessing(raw_grid)

def soucin_v_radku(radek):
    nej_soucin = 0
    for i in range(0, len(radek)-4):
        soucin =  radek[i]*radek[i+1]*radek[i+2]*radek[i+3] 
        if soucin > nej_soucin:
            nej_soucin = soucin
    return nej_soucin 


soucin_v_radku(grid[0])

def nej_soucin_v_mrizce(grid):  #34,345,080
    "in:grid, out:max product"
    nej_soucin = 0
    for radek in grid:
        soucin = soucin_v_radku(radek)
        if soucin > nej_soucin:
            nej_soucin = soucin
    return nej_soucin 

nej_soucin_v_mrizce(processed_grid)

def soucin_v_radku_f(radek):
    return max([radek[i]*radek[i+1]*radek[i+2]*radek[i+3] for i in range(0, len(radek)-4)])

def nej_soucin_v_mrizce_f(grid):
    return max([soucin_v_radku_f(radka) for radka in grid])

def nej_soucin_diagonalne(grid):
    nej_soucin = 0
    for i in range(0, 16):
        soucin =  grid[i][i]*grid[i+1][i+1]*grid[i+2][i+2]*grid[i+3][i+3] 
        if soucin > nej_soucin:
            nej_soucin = soucin
    return nej_soucin 

grid = processed_grid
nej_soucin_diagonalne(grid)

def soucin_diagonalne_f(grid):
    return max([grid[i][l]*grid[i+1][l+1]*grid[i+2][l+2]*grid[i+3][l+3] for i in range(0, len(grid)-4) for l in range(0,16)])
#32719995
soucin_diagonalne_f(grid)


def nej_soucin_sloupec(grid):
    nej_soucin = 0
    for l in range(0,20):
        for i in range(0, 16):
            soucin =  grid[i][l]*grid[i+1][l]*grid[i+2][l]*grid[i+3][l] 
            if soucin > nej_soucin:
                nej_soucin = soucin
    return nej_soucin  #51267216

nej_soucin_sloupec(grid)

def nej_soucin_sloupec_f(grid):
    return max([grid[i][l]*grid[i+1][l]*grid[i+2][l]*grid[i+3][l] for i in range(0, len(grid)-4) for l in range(0,16)])

nej_soucin_sloupec_f(grid)

def highest_grid_product():
    return max(nej_soucin_v_mrizce(grid), nej_soucin_sloupec(grid), soucin_diagonalne_f(grid))

highest_grid_product()


'''