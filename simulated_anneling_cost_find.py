import numpy as np
import random
import swapping
import plotfuncts
import coolfunc
import importfunc
import copy
import savecostfinding
import confidenceiv
#not used yet so commented out

def accept(cost1,cost2,T,costdiff):
    #checks if new path is accepted
    
    if cost1<cost2:
        return True
    #return False
    chance = np.exp((cost2-cost1)/T)
    costdiff.append(cost1-cost2)
    # if T > 1000:
    #     print(chance)
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
    
    while i<10000:
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

def markovCostcheck(path):
    data = [[],[]]

    # for t in np.arange(0.1, 1, .1):
    #     print(t)
    #     costdiff = []
    #     accepted = 0
    #     curpath = np.copy(path)
    #     np.random.shuffle(curpath)
    #     curcost = costCalc(curpath)
    #     for i in range(0, 100000):
    #         newpath = swapping.twoOptswap(np.copy(curpath))
    #         newcost = costCalc(newpath)
    #
    #         if accept(newcost, curcost, t, costdiff):
    #             curpath = newpath
    #             curcost = newcost
    #             accepted += 1
    #     data[0].append(t)
    #     data[1].append(accepted/100000)
    #     print(accepted/100000)
    for t in np.arange(600, 1500, 25):
        curpath = np.copy(path)
        curcost = costCalc(curpath)
        print(t)
        costdiff = []
        accepted = 0
        for i in range(0, 10000):
            newpath = swapping.twoOptswap(np.copy(curpath))
            newcost = costCalc(newpath)

            if accept(newcost, curcost, t, costdiff):
                curpath = newpath
                curcost = newcost
                accepted += 1
        data[0].append(t)
        data[1].append(accepted/10000)
        print(accepted / 10000)

    return data


def experimentannealing(minlen, maxlen, stepsz, init_path, costs, costdiff,data):

    for markov in np.arange(minlen, maxlen, stepsz):
        print(markov)
        data.append(['exponential', markov])
        annealedcost, annealedpath = confidence_interval_func(init_path,costs,markov,costdiff,data)
        print(annealedcost)

def confidence_interval_func(init_path, costs, markov, costdiff, data):
    best_path = []
    best_cost = 0
    costarray = []
    t = 10
    current_path = np.copy(init_path)
    annealedcost, annealedpath, best_cost, best_path = simulated_annealing(current_path, t, costs, markov, costdiff)
    for i in range(0,100):
        print(len(costarray))
        current_path = np.copy(init_path)
        np.random.shuffle(current_path)

        if i<10:
            save.saveCost(['exponential',markov,costs])
            save.saveCostDiff(['exponential',markov,costdiff])

        costs = [[],[]]
        costdiff=[]

        annealedcost, annealedpath, tmpcost, tmppath = simulated_annealing(current_path, t, costs, markov, costdiff)
        if tmpcost<best_cost:
            best_path = tmppath
            best_cost = tmpcost
        costarray.append(annealedcost)

    npcosts = np.array(costarray)
    #print(npcosts)
    average = np.mean(npcosts)
    variance = np.sqrt(np.var(npcosts))
    print("this is the average", average)

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
    #data[len(data)-1].append(best_cost,pathOnly,average,variance,tolerance, len(costarray))
    data = appendData(data, best_cost,pathOnly,average,variance,tolerance, len(costarray))
    save.savePath(data)
    data = []
    return average, variance

def appendData(data, best_cost,best_path,average,variance,tolerance, itters):
    data[len(data)-1].append(best_cost)
    data[len(data) - 1].append(best_path)
    data[len(data) - 1].append(average)
    data[len(data) - 1].append(variance)
    data[len(data) - 1].append(tolerance)
    data[len(data) - 1].append(itters)
    return data


def main():
    markovlen = 20
    data = []
    init_path442 = importfunc.importCities("TSP-Configurations/pcb442.tsp.txt")
    init_path280 = importfunc.importCities("TSP-Configurations/a280.tsp.txt")
    init_path51 = importfunc.importCities("TSP-Configurations/eil51.tsp.txt")

    path = init_path442
    initial_cost = costCalc(path)
    print("The initial cost is: ", initial_cost)

    data = markovCostcheck(path)

    savecostfinding.savePath(data)

if __name__ == "__main__":
    main()