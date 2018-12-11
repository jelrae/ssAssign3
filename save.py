# -*- coding: utf-8 -*-
"""
Created on Tue Dec 11 14:05:24 2018

@author: Gebruiker
"""

import csv

def saveCost(costs):
    
    filename = "costoveritersexpcooling.csv"
    
    with open(filename, 'a', newline = '') as csvfile:
            writer = csv.writer(csvfile, delimiter=',', quotechar='"')
        
            writer.writerow(costs)
    
def savePath(data):

    
    filename = "pathoveritersexpcooling.csv"
    
    with open(filename, 'a', newline = '') as csvfile:
            writer = csv.writer(csvfile, delimiter=',', quotechar='"')

            for line in data:

                writer.writerow(line)

    
def saveCostDiff(costdiff):
    
    filename = "differenceexpcooling.csv"
    
    with open(filename, 'a', newline = '') as csvfile:
            writer = csv.writer(csvfile, delimiter=',', quotechar='"')
            
            writer.writerow(costdiff)