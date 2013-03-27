from solutions import Pmf, relay, myplot


def BiasPmf(pmf, speed, name=None):
    newPmf = pmf.Copy(name=name)

    for x, p in newPmf.Items():
        diff = abs(x - speed)
        newPmf.Mult(x, diff)

    newPmf.Normalize()
    return newPmf


def main():
    results = relay.ReadResults()
    speeds = relay.GetSpeeds(results)

    pmf = Pmf.MakePmfFromList(speeds, 'actual speeds')

    biased = BiasPmf(pmf, 7.5, name='observed speeds')

    myplot.Clf()
    myplot.Hist(biased)
    myplot.Show(root='observed_speeds',
                title='PMF of running speed',
                xlabel='speed (mph)',
                ylabel='probability')


if __name__ == '__main__':
    main()
