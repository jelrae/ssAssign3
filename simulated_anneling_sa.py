import numpy as np
import random
import swapping
import plotfuncts
import coolfunc
import importfunc
import copy
import save
import confidenceiv
#not used yet so commented out

def accept(cost1,cost2,T,costdiff):
    #checks if new path is accepted
    
    if cost1<cost2:
        return True
    #return False
    chance = np.exp((cost2-cost1)/T)
    costdiff.append(cost1-cost2)
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

def reheating_annealing(init_path, costs, mlen,costdiff):
    for t in np.arange(100,10,-30):

        annealedcost, annealedpath = simulated_annealing(init_path, t,costs, mlen,costdiff)
        #print(optcost)
        print("The annealed cost for start temp: ", t, "is ", annealedcost)
        #print(annealedpath)
        #plotfuncts.plotRoute(init_path)
        #plotfuncts.plotRoute(annealedpath)
        plotfuncts.plotCosts(costs)
        init_path = annealedpath

def simulated_annealing(path,Tstart,costs,mlen,costdiff):

    #Initial simulated anneling fuction
    best_path = np.copy(path)
    best_cost = 0
    T = Tstart
    i = 0
    pathcost = costCalc(path)
    costs[0].append(pathcost)
    costs[1].append(len(costs[0]))
    
    while T>0.001:
        newpath = swapping.twoOptswap(copy.copy(path))
        newcost = costCalc(newpath)
        
        i+=1
        if i%mlen == 0:
            T = coolfunc.cool1(T)
        if newcost<pathcost:
            best_cost = newcost
            best_path = np.copy(newpath)
        if accept(newcost, pathcost, T, costdiff):
            path = newpath
            pathcost = newcost

        costs[0].append(pathcost)
        costs[1].append(len(costs[0]))
    
    return pathcost, path, best_cost, best_path

def experimentannealing(minlen, maxlen, stepsz, init_path, costs, costdiff,data):

    Tstart = 20
    for markov in np.arange(minlen, maxlen, stepsz):
        data.append(['exponential', markov])
        annealedcost, annealedpath = confidence_interval_func(init_path,costs,markov,costdiff,data)
    print(annealedcost, annealedpath)

def confidence_interval_func(init_path, costs, markov, costdiff, data):
    best_path = []
    best_cost = 0
    costarray = []
    t = 20
    current_path = np.copy(init_path)
    annealedcost, annealedpath, best_cost, best_path = simulated_annealing(current_path, t, costs, markov, costdiff)
    for i in range(0,100):
        print(len(costarray))
        current_path = np.copy(init_path)
        np.random.shuffle(current_path)

        if i<10:
            save.saveCost(['exponential',markov,costs])
            save.saveCostDiff(['exponential',markov,costdiff])

        annealedcost, annealedpath, tmpcost, tmppath = simulated_annealing(current_path, t, costs, markov, costdiff)
        if tmpcost<best_cost:
            best_path = tmppath
            best_cost = tmpcost
        costarray.append(annealedcost)

    npcosts = np.array(costarray)
    #print(npcosts)
    average = np.mean(npcosts)
    variance = np.sqrt(np.var(npcosts))
    #print("this is the variance", variance)

    while confidenceiv.checkstop(variance, len(costarray), average*0.01, average):

        print(len(costarray))
        current_path = np.copy(init_path)
        np.random.shuffle(current_path)
        annealedcost, annealedpath, tmpcost, tmppath = simulated_annealing(current_path, t, costs, markov, costdiff)
        if tmpcost<best_cost:
            best_path = tmppath
            best_cost = tmpcost
        costarray.append(annealedcost)
        average, variance = confidenceiv.calcurmv(average, variance, annealedcost, len(costarray))
    tolerance = (2 * 2.975 * variance / (len(costarray)) ** 0.5)

    pathOnly = [best_path[i][0] for i in range(len(annealedpath))]
    data[len(data)-1].append(best_cost,pathOnly,average,variance,tolerance, len(costarray))
    return average, variance


def main():
    markovlen = 20
    data = []
    init_path = importfunc.importCities("TSP-Configurations/a280.tsp.txt")
    
    optpath = importfunc.importOptimumPath("TSP-Configurations/a280.opt.tour.txt",init_path)

    #plotfuncts.plotRoute(init_path)
    optcost = costCalc(optpath)
    print(optcost)
    #plotfuncts.plotRoute(optpath)
    
    initial_cost = costCalc(init_path)
    costs = [[],[]]
    costdiff = []
    print("The initial cost is: ", initial_cost)

    experimentannealing(20, 21, 1, init_path, costs, costdiff,data)

    #x, s = confidence_interval_func(init_path, costs, markovlen,costdiff,data)

    print(x, s)
    save.savePath(data)

if __name__ == "__main__":
    main()