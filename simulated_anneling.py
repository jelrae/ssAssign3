import numpy as np
import random
import matplotlib.pyplot as plt
#not used yet so commented out
# import scipy as sp
# import pandas as pd

def importOptimumPath(filename):
    #imports the optimum path information
    path = np.genfromtxt(filename, dtype = int, skip_header=5, delimiter = ' ', skip_footer = 1)
    return path

def importCities(filename):
    #imports the data and sets up the basic data types needed
    citiesloc = np.genfromtxt(filename, dtype = int, skip_header=6, delimiter = ' ', skip_footer = 1)
    
    initial_guess = np.array(citiesloc[:,0])

    #shuffles the initial vector
    np.random.shuffle(citiesloc)

    return np.delete(citiesloc, 0, 1), citiesloc

def cool1(T):
    #cools the temperature
    alpha =0.99
    return alpha*T

def accept(cost1,cost2,T):
    #checks if new path is accepted
    if cost1<cost2:
        return True
    
    chance = np.exp((cost2-cost1)/T)
    #print(chance)
    if random.random()<chance:
        return True
    
    return False

def costCalc(cities):
    # initial cost calc function
    cost=0
    
    for i in range(len(cities)):

        cost+= ((cities[i][1]-cities[(i+1)%len(cities)][1])**2 + (cities[i][2]-cities[(i+1)%len(cities)][2])**2)**0.5
    
    return cost

def swap1(cities):
    
    #Initial city swap function
    index1 = random.randint(0,len(cities)-1)
    index2 = random.randint(0,len(cities)-1)
    
    while index1 == index2:
        index2 = random.randint(0,len(cities)-1)
    
    cities[[index1,index2]] = cities[[index2,index1]]

    return cities

def simulated_anneling(path,Tstart):
    #Initial simulated anneling fuction
    T = Tstart
    i = 0
    pathcost = costCalc(path)
    print(pathcost)
    while T>14:
        newpath = swap1(path)
        newcost = costCalc(newpath)
        if accept(newcost, pathcost, T):
            i+=1
            path = newpath
            pathcost = newcost
            if i%20 == 0:
                T = cool1(T)
                #print(T)

    return pathcost, path

def plotRoute(cities):
    
    xlist = []
    ylist = []
    
    for i in range(len(cities)):
        xlist.append(cities[i][1])
        ylist.append(cities[i][2])
        
    plt.figure()
    plt.plot(xlist,ylist)
    plt.show()

def main():

    cities_pos, init_path = importCities("TSP-Configurations/eil51.tsp.txt")
    optpath = importOptimumPath("TSP-Configurations/eil51.opt.tour.txt")

    plotRoute(init_path)
    #optcost = costCalc(optpath)

    annealedcost, annealedpath = simulated_anneling(init_path, 1000)

    #print(optcost)
    print(annealedcost)
    print(annealedpath)
    
    plotRoute(init_path)
    plotRoute(annealedpath)


if __name__ == "__main__":
    main()