from solutions import Pmf, myplot


def BiasPmf(pmf, name, invert=False):
    newPmf = pmf.Copy()
    newPmf.name = name

    for x, p in pmf.Items():
        if invert:
            newPmf.Mult(x, 1.0/x)
        else:
            newPmf.Mult(x, x)

    newPmf.Normalize()
    return newPmf


def UnbiasedPmf(pmf, name):
    return BiasPmf(pmf, name, invert=True)


def ClassSizes():

    d = {
        7: 8,
        12: 8,
        17: 14,
        22: 4,
        27: 6,
        32: 12,
        37: 8,
        42: 3,
        47: 2
    }

    pmf = Pmf.MakePmfFromDict(d, 'actual')
    print 'mean:', pmf.Mean()
    print 'var:', pmf.Var()

    biased = BiasPmf(pmf, 'biased')
    print 'mean:', biased.Mean()
    print 'var:', biased.Var()

    unbiased = UnbiasedPmf(pmf, 'unbiased')
    print 'mean:', unbiased.Mean()
    print 'var:', unbiased.Var()

    myplot.Pmfs([pmf, biased])
    myplot.Show(xlabel='Class size',
                ylabel='PMF')

def main():
    ClassSizes()


if __name__ == '__main__':
    main()
