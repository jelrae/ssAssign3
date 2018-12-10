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

def intersection(cities):
    
    # Creates a list of all intersection in route
    
    number = len(cities)
    intersections = []
    
    for i in range(number):
        
        i2 = (i+1)%number
        i3 = (i+2)%number
        i4 = (i+3)%number
        
        diff1 = [abs(cities[i][1]-cities[i2][1]),abs(cities[i][2]-cities[i2][2])]
        diff2 = [abs(cities[i3][1]-cities[i4][1]),abs(cities[i3][2]-cities[i4][2])]
        #print(diff1[0]*diff2[1] - diff2[0]*diff1[1])
        if diff1[0]*diff2[1] - diff2[0]*diff1[1] != 0:
            #print(diff1[0]*diff2[1] - diff2[0]*diff1[1])
            intersections.append(i)
            
    return intersections

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