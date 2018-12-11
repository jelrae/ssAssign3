# -*- coding: utf-8 -*-
"""
Created on Tue Dec 11 14:05:24 2018

@author: Gebruiker
"""

import csv

def saveCost(costs):
    
    filename = "costcoolingfunctionmaybeheating.csv"
    
    with open(filename, 'a', newline = '') as csvfile:
            writer = csv.writer(csvfile, delimiter=',', quotechar='"')
        
            writer.writerow(costs)
    
def savePath(data):

    
    filename = "pathcoolingfunctionmaybeheating.csv"
    
    with open(filename, 'a', newline = '') as csvfile:
            writer = csv.writer(csvfile, delimiter=',', quotechar='"')

            for line in data:

                writer.writerow(line)

    
def saveCostDiff(costdiff):
    
    filename = "diffcoolingfunctionmaybeheating.csv"
    
    with open(filename, 'a', newline = '') as csvfile:
            writer = csv.writer(csvfile, delimiter=',', quotechar='"')
            
            writer.writerow(costdiff)