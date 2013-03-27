from solutions import Pmf, descriptive


def calcBin(pmf, low, high):
    total = 0
    for week in range(low, high+1):
        total += pmf.Prob(week)
    return total


def Probs(pmf):
    early = calcBin(pmf, 0, 37)
    onTime =  calcBin(pmf, 38, 40)
    late = calcBin(pmf, 41, 50)

    return early, onTime, late


def RelativeRisk(pmf1, pmf2):
    pmf1 = Probs(pmf1)
    pmf2 = Probs(pmf2)
    ratios = []

    for x, y in zip(pmf1, pmf2):
        ratios.append(x / y)

    return ratios


def Summary(pmf1, pmf2):
    firsts = Probs(pmf1)
    others = Probs(pmf2)
    risks = RelativeRisk(pmf1, pmf2)

    print 'probability of being early'
    print 'firsts:', firsts[0]
    print 'others:', others[0]

    print '\n' 'probability of being on time'
    print 'firsts:', firsts[1]
    print 'others:', others[1]

    print '\n' 'probability of being late'
    print 'firsts:', firsts[2]
    print 'others:', others[2]

    print '\n' 'Risks (firsts:others)'
    print 'Prob Early:', risks[0]
    print 'Prob On Time:', risks[1]
    print 'Prob late:', risks[2]


def main():
    pool, firsts, others = descriptive.MakeTables()

    Summary(firsts.pmf, others.pmf)


if __name__ == "__main__":
    main()