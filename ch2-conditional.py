from solutions import Pmf, descriptive, myplot, risk
import matplotlib.pyplot as pyplot

def conditional(pmf, week, name='conditional'):
    copy = pmf.Copy(name)

    for i in pmf.Values():
        if i < week:
            copy.Remove(i)
    copy.Normalize()
    return copy


def plotLines(firsts, others):
    weeks = range(35, 46)

    probs = {}
    for table in [firsts, others]:
        name = table.pmf.name
        probs[name] = []
        for week in weeks:
            cond = conditional(table.pmf, week)
            prob = cond.Prob(week)
            print week, prob, table.pmf.name
            probs[name].append(prob)
            print probs

    pyplot.clf()
    for name, ps in probs.items():
        pyplot.plot(weeks, ps, label=name)
        print name, ps

    myplot.Save(root='conditional',
                xlabel='weeks',
                ylabel=r'Prob{x $=$ weeks | x $\geq$ weeks}',
                title='Conditional Probability')


def main():
    pool, firsts, others = descriptive.MakeTables()
    plotLines(firsts, others)


if __name__ == "__main__":
    main()