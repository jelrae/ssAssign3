import numpy as np
import scipy as sp

def importCities(filename):
    file = open(filename, "r")

    cities = file.read()

    print(cities)

    return cities


importCities("TSP-Configurations/eil51.tsp.txt")

def markov_chain():

    return "thing"

def simulated_anneling():

    return "bla"