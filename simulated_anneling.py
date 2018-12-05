import numpy as np
#not used yet so commented out
# import scipy as sp
# import pandas as pd
# import random as rd

def importOptimumPath(filename):
    #imports the optimum path information
    path = np.genfromtxt(filename, dtype = int, skip_header=5, delimiter = ' ', skip_footer = 1)
    return path

def importCities(filename):
    #imports the data and sets up the basic data types needed
    citiesloc = np.genfromtxt(filename, dtype = int, skip_header=6, delimiter = ' ', skip_footer = 1)

    initial_guess = np.array(citiesloc[:,0])

    #shuffles the initial vector
    np.random.shuffle(initial_guess)

    return np.delete(citiesloc, 0, 1), initial_guess

def cool1(T):
    #cools the temperature
    alpha =0.99
    return alpha*T

def accept(cost1,cost2,T):
    #checks if new path is accepted
    if cost1<cost2:
        return True
    
    chance = np.exp((cost1-cost2)/T)
    print(chance)
    
    if random.random()<chance:
        return True
    
    return False

def costCalc(cities):
    # initial cost calc function
    cost=0
    
    for i in range(len(cities)):

        cost+= ((cities[i][0]-cities[(i+1)%len(cities)][0])**2 + (cities[i][1]-cities[(i+1)%len(cities)][1])**2)**0.5
        
    return cost

def swap1(cities):
    #Initial city swap function
    index1 = random.randn(len(cities))
    index2 = random.randn(len(cities))
    
    while index1 == index2:
        index2 = random.randn(len(cities))
        
    cities[index1],cities[index2] = cities[index2],cities[index1]

    return citiesloc, initial_guess

def simulated_anneling(path,Tstart):
    #Initial simulated anneling fuction
    T = Tstart
    i = 0
    pathcost = costCalc(path)
    while T>0.01:
        newpath = swap1(path)
        newcost = costCalc(newpath)
        if accept(newcost, pathcost, T):
            i+=1
            path = newpath
            pathcost = newcost
            if i%20 == 0:
                T = cool1(T)


    return pathcost, path

def main():

    cities_pos, init_path = importCities("TSP-Configurations/eil51.tsp.txt")
    optpath = importOptimumPath("TSP-Configurations/eil51.opt.tour.txt")

    optcost = costCalc(optpath)

    annealedcost, annealedpath = simulated_anneling(init_path, 10)

    print(optcost)
    print(annealedcost)


if __name__ == "__main__":
    main()