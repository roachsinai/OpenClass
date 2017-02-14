from math import pow

class RootFinder:
    """
    implement find root, like sqrt function, cube function.abs
    Find g which let g^n == w.

    Square Root: http://www.cs.wustl.edu/~kjg/CS101_SP97/Notes/SquareRoot/sqrt.html
    """

    def __init__(self, n):
        self.n = n

    def f(self, w, g):
        return pow(g, self.n) - w

    def fPrime(self, g):
        return pow(g, self.n-1) * self.n

    def closeEnough(self, a, b):
        if abs(a-b) < abs(b*0.0001):
            return True
        else:
            return False

    def findRoot(self, w, g):
        print('  guessing: ' + repr(g))
        newGuess = g - self.f(w, g) / self.fPrime(g)
        if self.closeEnough(newGuess, g):
            return newGuess
        else:
            return self.findRoot(w, newGuess)

    def root(self, w):
        return self.findRoot(w, 1)

sqrt = RootFinder(2)
sqrt.root(2)