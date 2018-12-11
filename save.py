# -*- coding: utf-8 -*-
"""
Created on Tue Dec 11 14:05:24 2018

@author: Gebruiker
"""

import csv

def saveData(markov, thePath, costs, costdiff):
    
    saveMain(markov, thePath, costs)
    saveCostDiff(markov,costdiff)
    
def saveMain(markov, thePath, costs):
    
    filename = "coolingfunctionmaybeheating.csv"
    
    with open(filename, 'a', newline = '') as csvfile:
            writer = csv.writer(csvfile, delimiter=',', quotechar='"')
        
            writer.writerow([markov,thePath,costs])

    
def saveCostDiff(markov, costdiff):
    
    filename = "coolingfunctionandmaybeheating.csv"
    
    with open(filename, 'a', newline = '') as csvfile:
            writer = csv.writer(csvfile, delimiter=',', quotechar='"')
            
            writer.writerow([markov,costdiff])