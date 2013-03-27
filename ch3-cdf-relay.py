from solutions import relay, Cdf, myplot


def main():
    results = relay.ReadResults()
    speeds = relay.GetSpeeds(results)

    cdf = Cdf.MakeCdfFromList(speeds, 'speeds')

    myplot.Cdf(cdf)
    myplot.Save(root='relay_cdf',
                title='CDF of running speed',
                xlabel='speed (mph)',
                ylabel='probability')

if __name__ == '__main__':
    main()