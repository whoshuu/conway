#!/usr/bin/env python


from __future__ import print_function
from copy import deepcopy
from os import system
from random import getrandbits
from time import sleep

SIZE = 30

cells = [] 
for i in range(SIZE):
    cells.append([])
    for _ in range(SIZE):
        cells[i].append(int(getrandbits(1)))

while True:
    new_cells = deepcopy(cells)
    for x in range(SIZE):
        for y in range(SIZE):
            neighbors = 0
            for j in range(-1, 2):
                for k in range(-1, 2):
                    if j == 0 and k == 0:
                        continue
                    if x + j < 0 or x + j >= SIZE:
                        continue
                    if y + k < 0 or y + k >= SIZE:
                        continue
                    if cells[x + j][y + k] == 1:
                        neighbors = neighbors + 1
            if cells[x][y] == 1:
                if neighbors < 2 or neighbors > 3:
                    new_cells[x][y] = 0
            elif neighbors == 3:
                new_cells[x][y] = 1
    cells = deepcopy(new_cells)
    sleep(0.1)
    system('clear')
    for x in cells:
        for cell in x:
            if cell == 1:
                print('x', end='')
            else:
                print(' ', end='')
        print('')
