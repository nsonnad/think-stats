from solutions import Pmf
import random

# make a list of random ints
# lifetimes = [random.randint(0,12) for _ in range(250)]
l = [11, 7, 10, 6, 6, 0, 5, 6, 9, 4, 6, 4, 4, 1, 9, 11, 9, 3, 10, 4, 7, 9, 12, 4, 9, 3, 3, 6, 1, 7, 10, 11, 11, 2, 6, 0, 5, 8, 9, 8, 12, 9, 7, 2, 8, 5, 1, 5, 4, 6, 9, 6, 5, 12, 0, 3, 11, 12, 0, 4, 11, 3, 2, 2, 4, 9, 2, 8, 2, 7, 12, 0, 4, 5, 7, 6, 11, 0, 9, 12, 7, 3, 6, 12, 11, 4, 4, 8, 7, 8, 5, 9, 10, 6, 6, 9, 10, 6, 0, 2, 6, 0, 7, 7, 4, 0, 11, 11, 9, 12, 2, 7, 10, 6, 9, 9, 1, 11, 7, 0, 0, 5, 8, 8, 11, 8, 8, 1, 0, 9, 8, 0, 0, 7, 2, 3, 8, 0, 9, 12, 3, 3, 8, 12, 2, 6, 12, 3, 0, 7, 2, 12, 7, 12, 3, 3, 2, 9, 10, 4, 3, 2, 6, 7, 10, 11, 1, 4, 8, 9, 11, 0, 4, 1, 3, 6, 12, 0, 8, 8, 11, 3, 9, 12, 6, 4, 0, 3, 2, 6, 8, 2, 3, 3, 8, 3, 2, 6, 6, 7, 6, 1, 12, 3, 10, 4, 10, 1, 12, 9, 9, 5, 11, 7, 10, 9, 0, 6, 0, 3, 3, 11, 5, 12, 8, 10, 9, 6, 2, 10, 1, 6, 8, 5, 0, 4, 12, 1, 3, 6, 7, 3, 8, 12, 9, 0, 12, 0, 4, 5]

pmf = Pmf.MakePmfFromList(l)
age = 4

# remove values that are younger than the age we want
# and re-normalize PMF
def RemainingLifetime(lifetimes, year):
    for i in lifetimes.Values():
        if year > i:
            lifetimes.Remove(i)
    lifetimes.Normalize()
    return lifetimes.Print()


print 'Original distribution'
print pmf.Print()

print 'Distribution at age', age
print RemainingLifetime(pmf, age)
