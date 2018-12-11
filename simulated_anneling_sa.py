import numpy as np
import random
import swapping
import plotfuncts
import coolfunc
import importfunc
import copy
#not used yet so commented out

def accept(cost1,cost2,T):
    #checks if new path is accepted
    
    if cost1<cost2:
        return True
    #return False
    chance = np.exp((cost2-cost1)/T)
    if T > 1000:
        print(chance)
    if random.random()<chance:
        #print("accepted")
        return True
    
    return False

def costCalc(cities):
    # initial cost calc function
    cost=0
    #print(cities)
    
    for i in range(len(cities)-1):

        cost+= ((cities[i][1]-cities[i+1][1])**2 + (cities[i][2]-cities[i+1][2])**2)**0.5
    
    return cost

def reheating_annealing(init_path, costs, mlen):
    for t in np.arange(100,10,-30):

        annealedcost, annealedpath = simulated_annealing(init_path, t,costs, mlen)

        #print(optcost)
        print("The annealed cost for start temp: ", t, "is ", annealedcost)
        #print(annealedpath)
        #plotfuncts.plotRoute(init_path)
        #plotfuncts.plotRoute(annealedpath)
        plotfuncts.plotCosts(costs)
        init_path = annealedpath

def simulated_annealing(path,Tstart,costs,mlen):
    #Initial simulated anneling fuction
    T = Tstart
    i = 0
    pathcost = costCalc(path)
    costs[0].append(pathcost)
    costs[1].append(len(costs[0]))
    
    while T>0.01:
        newpath = swapping.twoOptswap(copy.copy(path))
        newcost = costCalc(newpath)
        
        i+=1
        if i%mlen == 0:
            T = coolfunc.cool1(T)
        if accept(newcost, pathcost, T):
            path = newpath
            pathcost = newcost
            
        costs[0].append(pathcost)
        costs[1].append(len(costs[0]))
    
    return pathcost, path

def varychainlength(minlen, maxlen, stepsz, init_path, Tstart, costs):

    for markov in np.arange(minlen, maxlen, stepsz):
        annealedcost, annealedpath = simulated_annealing(init_path, Tstart, costs, markov)

def main():
    markovlen = 20
    init_path = importfunc.importCities("TSP-Configurations/eil51.tsp.txt")
    optpath = importfunc.importOptimumPath("TSP-Configurations/eil51.opt.tour.txt",init_path)

    plotfuncts.plotRoute(init_path)
    optcost = costCalc(optpath)
    print(optcost)
    plotfuncts.plotRoute(optpath)
    
    initial_cost = costCalc(init_path)
    costs = [[],[]]
    print("The initial cost is: ", initial_cost)

    reheating_annealing(init_path, costs, markovlen)

def testfunct():
    a = np.arange(0,100,1)

    print(a)

    b = twoOptswap(a)

    print(b)

if __name__ == "__main__":
    main()