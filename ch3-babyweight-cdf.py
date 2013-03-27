from solutions import myplot, survey
import Cdf

def birth_weights(table):
    weights = []
    for x in table:
        if not x.birthwgt_oz == 'NA':
            weights.append(x.birthwgt_oz)

    return weights


def weights_percentile(weights, val):
    count = 0
    for x in weights:
        if x <= val:
            count += 1

    percentile = 100 * count / len(weights)
    return percentile


def compute_and_plot_cdf(weights):
    cdf = Cdf.MakeCdfFromList(weights, 'birth weights')
    new_sample = cdf.Sample(3000)

    new_cdf = Cdf.MakeCdfFromList(new_sample, 'birth weights')

    # myplot.Cdf(new_cdf)
    # myplot.Cdf(cdf)
    # myplot.Save(root='ch3-babyweight-cdf',
    #             title='CDF of baby weights',
    #             xlabel='baby weight (oz)',
    #             ylabel='probability')
    print cdf.Median()
    print cdf.Interquartile()


def main():
    results = survey.Pregnancies()
    results.ReadRecords()
    table = results.records

    weights = birth_weights(table)
    # percentile = weights_percentile(weights, 12)
    compute_and_plot_cdf(weights)

if __name__ == '__main__':
    main()