import numpy as np
import scipy as sp
import pandas as pd
import random as rd

def importCities(filename):

    citiesloc = np.genfromtxt(filename, dtype = int, skip_header=6, delimiter = ' ', skip_footer = 1)

    initial_guess = citiesloc[:,0]

    #print(citiesloc)

<<<<<<< Updated upstream
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

=======
    print(initial_guess)
>>>>>>> Stashed changes

    return citiesloc, initial_guess

cities_pos = importCities("TSP-Configurations/eil51.tsp.txt")

#initial_vect =

def markov_chain():



    return "thing"

def simulated_anneling():

    return "bla"