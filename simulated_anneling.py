import numpy as np
import random
import matplotlib.pyplot as plt
#not used yet so commented out
# import scipy as sp
# import pandas as pd

def importOptimumPath(filename, coordinates):
    #imports the optimum path information
    path = np.genfromtxt(filename, dtype = int, skip_header=5, delimiter = ' ', skip_footer = 1)
    pathAll = []
    
    for i in range(len(path)):
        for j in range(len(coordinates)):
            
            if path[i] == coordinates[j][0]:
                pathAll.append(coordinates[j])
                break
            
    pathAll = np.array(pathAll)
    return pathAll

def importCities(filename):
    #imports the data and sets up the basic data types needed
    citiesloc = np.genfromtxt(filename, dtype = int, skip_header=6, delimiter = ' ', skip_footer = 1)

    #shuffles the initial vector
    np.random.shuffle(citiesloc)

    return citiesloc

#Coolling schemes: https://www.fys.ku.dk/~andresen/BAhome/ownpapers/permanents/annealSched.pdf

def cool1(T):
    #cools the temperature
    alpha =0.99
    return alpha*T

def linear_cooling(Tmax, steps):
    #returns the value for a constant cooling over a
    return Tmax/steps

def accept(cost1,cost2,T):
    #checks if new path is accepted
    if cost1<cost2:
        return True
    
    chance = np.exp((cost2-cost1)/T)
    #print(chance)
    if random.random()<chance:
        #print("accepted")
        return True
    
    return False

def costCalc(cities,costs):
    # initial cost calc function
    cost=0
    
    for i in range(len(cities)-1):

        cost+= ((cities[i][1]-cities[i+1][1])**2 + (cities[i][2]-cities[i+1][2])**2)**0.5
    
    costs[0].append(cost)
    costs[1].append(len(costs[0]))
    return cost,costs

def swap1(cities):
    
    #Initial city swap function
    index1 = random.randint(0,len(cities)-1)
    index2 = random.randint(0,len(cities)-1)
    
    while index1 == index2:
        index2 = random.randint(0,len(cities)-1)
    
    cities[[index1,index2]] = cities[[index2,index1]]

    return cities

<<<<<<< Updated upstream
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

def swap2(cities):
    
    number = len(cities)
    
    intersections = intersection(cities)
    #print(len(intersections))
    if len(intersections) == 0:
        exit()
    
    index = (np.random.choice(intersections)+1)%number
    index2 = (index+2)%number
    
    cities[index:index2] = np.flip(cities[index:index2])
    
    return cities
        

def simulated_annealing(path,Tstart,costs):
    #Initial simulated anneling fuction
    T = Tstart
    i = 0
    pathcost,costs = costCalc(path,costs)
    #print(pathcost)
    for i in range(1):#while T>0.0001:
        newpath = swap1(path)
        newcost,costs = costCalc(newpath,costs)
        i+=1
        if i%20 == 0:
            T = cool1(T)
            print(T)
=======
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

def simulated_anneling(path,Tstart):
    #Initial simulated anneling fuction
    T = Tstart
    i = 0
    pathcost = costCalc(path)
    print(pathcost)
    while T>17:
        newpath = twoOptswap(path)
        newcost = costCalc(newpath)
        if accept(newcost, pathcost, T):
            
            path = newpath
            pathcost = newcost
                #print(T)

    return pathcost, path, costs

def plotRoute(cities):
    
    xlist = []
    ylist = []
    
    for i in range(len(cities)):
        xlist.append(cities[i][1])
        ylist.append(cities[i][2])
        
    plt.figure()
    plt.plot(xlist,ylist)
    plt.show()
    
def plotCosts(costs):
    
    plt.figure()
    plt.plot(costs[1],costs[0])
    plt.figure()

def main():

    init_path = importCities("TSP-Configurations/eil51.tsp.txt")
    optpath = importOptimumPath("TSP-Configurations/eil51.opt.tour.txt",init_path)

    plotRoute(init_path)
    optlist = [[],[]]
    optcost, optlist = costCalc(optpath,optlist)
    print(optcost)
    plotRoute(optpath)
    
    costs = [[],[]]
    
    annealedcost, annealedpath, costs = simulated_annealing(init_path, 1,costs)

    #print(optcost)
    print(annealedcost)
    print(annealedpath)
    plotRoute(init_path)
    plotRoute(annealedpath)
    plotCosts(costs)

def testfunct():
    a = np.arange(0,100,1)

    print(a)

    b = twoOptswap(a)

    print(b)

if __name__ == "__main__":
    main()