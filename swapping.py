import numpy as np
import random

def swap1(cities):
    # Initial city swap function
    index1 = random.randint(0, len(cities) - 1)
    index2 = random.randint(0, len(cities) - 1)

    while index1 == index2:
        index2 = random.randint(0, len(cities) - 1)

    cities[[index1, index2]] = cities[[index2, index1]]

    return cities


def swap2(cities):
    number = len(cities)

    intersections = intersection(cities)
    # print(len(intersections))
    if len(intersections) == 0:
        exit()

    index = (np.random.choice(intersections) + 1) % number
    index2 = (index + 2) % number

    cities[index:index2] = np.flip(cities[index:index2])

    return cities

def twoOptswap(cities):

    index1 = random.randint(0,len(cities)-1)
    index2 = random.randint(0,len(cities)-1)

    if index1<index2:
        rangeindex = cities[index1:index2]
        rangeindex = rangeindex[::-1]
        cities[index1:index2] = rangeindex

    else:
        rangeindex = cities[index2:index1]
        rangeindex = rangeindex[::-1]
        cities[index2:index1] = rangeindex

    return cities