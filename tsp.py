# -*- coding: utf-8 -*-
"""
Created on Tue Dec  4 15:27:45 2018

@author: Gebruiker
"""

def importCities(filename):
    
    file = open(filename,"r")
    
    cities = file.read()
    
    print(cities)
    
    return cities
    
importCities("TSP-Configurations/eil51.tsp.txt")