import math
import numpy
import scipy.integrate as scipy

N = 10
uR = 1
Omega = [0, 1]
beta = 0
gamma = 1


def a(x):
    return 0


def b(x):
    return 0


def c(x):
    return 1


def f(x):
    return x


def solveLinArr(A, B):   #rozwiązujemy układ liniowy B*U = L, chcemy U
    return(numpy.linalg.solve(A,B))


def integrate(f):   #całkujemy!
    return scipy.quad(f, 0, 1)


def takeX(n):    #bierzemy kolejną wartość x, gdzie kolejny trójkąt ma maximum
    return n/N


def eFun(i):
    return lambda x: e(x, i)


def e(x, n):
    return max(0, 1-abs(x-takeX(n))*N)


def diffEFun(n: int):
    return lambda x: diffE(x, n)


def diffE(x, n):
    if n > 0:
        if x < takeX(n-1) or x > takeX(n+1):
            return 0
        elif x < takeX(n):
            return N
        else:
            return -N
    else:
        if x < takeX(1):
            return -N
        else:
            return 0


def getL(n):
    if n == N:
        return uR
    en = eFun(n)
    return integrate(lambda x: f(x)*en(x))[0]-gamma*en(0)


def getB(i: int, j: int) -> float:
    e1 = diffEFun(i)
    e2 = diffEFun(j)
    e1Diff = diffEFun(i)
    e2Diff = diffEFun(j)

    first = -beta * e1(0) * e2(0)
    second = -1 * integrate(lambda x: a(x) * e1Diff(x) * e2Diff(x))[0]  #funkcja integrate zwraca parę, gdzie pierwsza liczba
                                                                        # jest wartością całki na przedziale (0,1)
    third = integrate(lambda x: b(x) * e1Diff(x) * e2(x))[0]
    fourth = integrate(lambda x: c(x) * e1(x) * e2(x))[0]

    return first + second + third + fourth


def BForMatrix(i, j):
    if i == N:
        if j == N:
            return 1
        return 0
    return getB(i, j)


def makeABMatrix():
    BMatrix = numpy.zeros((N+1, N+1))
    for i in range(N+1):
        for j in range(N+1):
            BMatrix[i][j] = BForMatrix(i, j)
    return BMatrix


def makeALMatrix():
    LMatrix = numpy.zeros((N+1))
    for i in range(N+1):
        LMatrix[i] = getL(i)
    return LMatrix


def solveForU():
    uFactors = solveLinArr(makeABMatrix(), makeALMatrix())
    u = lambda x: sum([uFactors[i] * e(x, i) for i in range(0, N + 1)]) #shift jest dodany w macierzy, więc jest uwzględniany już tam
    return u

