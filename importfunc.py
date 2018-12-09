import numpy as np

def importOptimumPath(filename, coordinates):
    # imports the optimum path information
    path = np.genfromtxt(filename, dtype=int, skip_header=5, delimiter=' ', skip_footer=1)
    pathAll = []

    for i in range(len(path)):
        for j in range(len(coordinates)):

            if path[i] == coordinates[j][0]:
                pathAll.append(coordinates[j])
                break

    pathAll = np.array(pathAll)
    return pathAll


def importCities(filename):
    # imports the data and sets up the basic data types needed
    citiesloc = np.genfromtxt(filename, dtype=int, skip_header=6, delimiter=' ', skip_footer=1)
    print(citiesloc)
    # shuffles the initial vector
    np.random.shuffle(citiesloc)
    print(citiesloc)

    return citiesloc