import matplotlib.pyplot as plt


def plotRoute(cities):
    xlist = []
    ylist = []

    for i in range(len(cities)):
        xlist.append(cities[i][1])
        ylist.append(cities[i][2])

    plt.figure()
    plt.plot(xlist, ylist)
    plt.show()


def plotCosts(costs):
    plt.figure()
    plt.plot(costs[1], costs[0])
    plt.show()