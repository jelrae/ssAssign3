#Coolling schemes: https://www.fys.ku.dk/~andresen/BAhome/ownpapers/permanents/annealSched.pdf
import math

def cool1(T):
    #cools the temperature
    alpha =0.956
    return alpha*T

def linear_cooling(Tmax, steps):
    #returns the value for a constant cooling over a
    alpha = .43745
    return Tmax - (alpha*steps)

def log_cooling(steps, c):

    d = 1
    return c/(math.log10(steps + d))

def coscooling(steps,Tmax):
    return Tmax*math.cos((steps*math.pi)/400)