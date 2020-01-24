from main.RRIR import solveForU
from main.RRIR import N
import matplotlib.pyplot as plt
import numpy as np
import math

#res = solveForU()
def res(x):
    return math.sin(2*x-math.pi)
for x in np.arange(-2*math.pi, -2*math.pi, math.pi/100):
    print("x: ", round(x, 2), "\t u(x) = ", round(res(x), 4))



t1 = np.arange(-2*math.pi, 2*math.pi, math.pi/100)
t2 = [round(res(x), 3) for x in t1]

with plt.style.context('Solarize_Light2'):
    plt.figure()
    #plt.subplot(211)
    plt.plot(t1, t2, "co")
    plt.xlabel("x")
    plt.ylabel("u(x)")
    plt.plot(t1, t2, 'c')

plt.show()
