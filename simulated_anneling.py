import numpy as np
import scipy as sp

def importCities(filename):
    file = open(filename, "r")

    cities = file.read()

    print(cities)

    return cities

def cool1(T):
    alpha =0.99
    return alpha*T

def accept(cost1,cost2,T):
    
    if cost1<cost2:
        return True
    
    chance = np.exp((cost1-cost2)/T)
    
    if random.random()<chance:
        return True
    
    return False

def costCalc(cities):
    cost=0
    
    for i in range(len(cities)):
        
        cost+= ((cities[i][1]-cities[(i+1)%len(cities)][1])**2 (cities[i][2]-cities[(i+1)%len(cities)][2])**2)**0.5
        
    return cost

def swap1(cities):
    
    index1 = random.randn(len(cities))
    index2 = random.randn(len(cities))
    
    while index1 == index2:
        index2 = random.randn(len(cities))
        
    cities[index1],cities[index2] = cities[index2],cities[index1]


importCities("TSP-Configurations/eil51.tsp.txt")

def markov_chain():

    return "thing"

def simulated_anneling():

    return "bla"