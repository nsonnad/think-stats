from solutions import survey, thinkstats
import math

def partition(table):
    firsts = survey.Pregnancies()
    others = survey.Pregnancies()

    for birth in table.records:
        if birth.outcome != 1:
            continue

        if birth.birthord == 1:
            firsts.AddRecord(birth)
        else:
            others.AddRecord(birth)

    return firsts, others


def process(table):
    table.lengths = [p.prglength for p in table.records]
    table.n = len(table.lengths)
    table.mu = thinkstats.Mean(table.lengths)
    # table.var = thinkstats.MeanVar(table.lengths)[1]
    # table.sd = math.sqrt(table.var)

def make_tables(data_dir='.'):
    table = survey.Pregnancies()
    table.ReadRecords(data_dir)

    firsts, others = partition(table)

    return firsts, others, table


def process_tables(*tables):
    for table in tables:
        process(table)


def summarize(data_dir):

    firsts, others, table = make_tables(data_dir)
    process_tables(firsts, others)

    print 'Number of first babies', firsts.n
    print 'Number of others', others.n

    mu1, mu2 = firsts.mu, others.mu

    print 'Mean gestation in weeks:'
    print 'First babies', mu1
    print 'Others', mu2

    print 'Difference in days', (mu1 - mu2) * 7.0

    # sd1, sd2 = firsts.sd, others.sd

    # print 'Standard deviations:'
    # print 'First babies', sd1
    # print 'Others', sd2

    # print 'Differences in SD:', (sd1 - sd2)

def main(name, data_dir='.'):
    summarize(data_dir)


if __name__ == '__main__':
    import sys
    main(*sys.argv)