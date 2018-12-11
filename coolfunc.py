#Coolling schemes: https://www.fys.ku.dk/~andresen/BAhome/ownpapers/permanents/annealSched.pdf

def cool1(T):
    #cools the temperature
    alpha =0.9
    return alpha*T

def linear_cooling(Tmax, steps):
    #returns the value for a constant cooling over a
    alpha = .1*Tmax
    return Tmax - (alpha*steps)

def log_cooling(steos, c):

    d = 1
    return c/(math.log10(steps+d))