import numpy as np
import random
import swapping
import plotfuncts
import coolfunc
import importfunc
#not used yet so commented out

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

def simulated_annealing(path,Tstart,costs):
    #Initial simulated anneling fuction
    T = Tstart
    i = 0
    pathcost,costs = costCalc(path,costs)
    while T>0.001:
        newpath = swapping.twoOptswap(path)
        newcost,costs = costCalc(newpath,costs)
        i+=1
        if i%20 == 0:
            T = coolfunc.cool1(T)
        if accept(newcost, pathcost, T):
            
            path = newpath
            pathcost = newcost

    return pathcost, path, costs

def main():

    init_path = importfunc.importCities("TSP-Configurations/eil51.tsp.txt")
    optpath = importfunc.importOptimumPath("TSP-Configurations/eil51.opt.tour.txt",init_path)

    plotfuncts.plotRoute(init_path)
    optlist = [[],[]]
    optcost, optlist = costCalc(optpath,optlist)
    print(optcost)
    plotfuncts.plotRoute(optpath)
    tmp = [[], []]
    initial_cost, tmp = costCalc(init_path, tmp)
    costs = [[],[]]
    print("The initial cost is: ", initial_cost)
    for t in np.arange(.1, 101, 5):

        annealedcost, annealedpath, costs = simulated_annealing(init_path, t,costs)

        #print(optcost)
        print("The annealed cost for start temp: ", t, "is ", annealedcost)
        #print(annealedpath)
        #plotfuncts.plotRoute(init_path)
        #plotfuncts.plotRoute(annealedpath)
        #plotfuncts.plotCosts(costs)

def testfunct():
    a = np.arange(0,100,1)

    print(a)

    b = twoOptswap(a)

    print(b)

if __name__ == "__main__":
    main()