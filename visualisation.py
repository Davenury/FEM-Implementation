from main.RRIR import solveForU
from main.RRIR import N
import matplotlib.pyplot as plt
import numpy as np

res = solveForU()
for x in np.arange(0, 1.1, 1/N):
    print("x: ", round(x, 2), "\t u(x) = ", round(res(x), 4))


t1 = np.arange(0.0, 1.0, 1.0/N)
t2 = [round(res(x), 3) for x in t1]

with plt.style.context('Solarize_Light2'):
    plt.figure()
    #plt.subplot(211)
    plt.plot(t1, t2, "co")
    plt.xlabel("x")
    plt.ylabel("u(x)")
    plt.plot(t1, t2, 'c')

plt.show()
