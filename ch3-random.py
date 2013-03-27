import random
from solutions import Pmf, Cdf, myplot

randlist = []

for x in range(1000):
    randlist.append(random.random())

pmf = Pmf.MakePmfFromList(randlist)
cdf = Cdf.MakeCdfFromList(randlist)

myplot.Cdf(cdf)
myplot.Pmf(pmf)

myplot.Save(root='ch3-random',
            title='CDF, PMF of randoms',
            xlabel='number',
            ylabel='probability')