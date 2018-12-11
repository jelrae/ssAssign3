# -*- coding: utf-8 -*-
"""
Created on Tue Dec 11 14:05:24 2018

@author: Gebruiker
"""

import csv

def saveCost(markov, costs):
    
    filename = "costcoolingfunctionmaybeheating" + str(markov) + ".csv"
    
    with open(filename, 'a', newline = '') as csvfile:
            writer = csv.writer(csvfile, delimiter=',', quotechar='"')
        
            writer.writerow(costs)
    
def savePath(markov, thePath, theCost, avCost, variance):
    
    pathOnly = [thePath[i][0] for i in range(len(thePath))]
    
    filename = "pathcoolingfunctionmaybeheating" + str(markov) + ".csv"
    
    with open(filename, 'a', newline = '') as csvfile:
            writer = csv.writer(csvfile, delimiter=',', quotechar='"')
        
            writer.writerow([theCost, avCost, variance,pathOnly])

    
def saveCostDiff(markov, costdiff):
    
    filename = "diffcoolingfunctionmaybeheating" + str(markov) + ".csv"
    
    with open(filename, 'a', newline = '') as csvfile:
            writer = csv.writer(csvfile, delimiter=',', quotechar='"')
            
            writer.writerow(costdiff)