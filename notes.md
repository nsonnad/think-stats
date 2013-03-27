Notes on the book [Think Stats](http://greenteapress.com/thinkstats/):


## Chapter 1
cross-sectional study observes a group at a single moment in time. logitudinal observes same group over time

group of survey respondents are called a cohort

oversampling allows you to draw statistical inferences, but damages ability to make conclusions about wider population

database stuff: information about one respondent is a record. variables that make up record are fields. collection of records is table.

variables in NSFG/elsewhere are recodes, meaning they are not part of the raw data but were calculated using it.

apparent effect: looks like something is going on, but we’re not sure yet.


## Chapter 2 - Descriptive statistics
summary statistics include mean, variance, median
Mean: =1nixi

an apparent effect that is caused by bias, measurement error or any other fuck up is called an artifact.

variance describes the spread of the data
    Variance: 2=1ni(xi -  )2     (sqrt of this result is standard deviation)

xi-µ is called variation from the mean

distribution looks at how often a given value appears

probability is frequency as a fraction of the sample size (n)

calculating probability of a given value is normalization. normalized histogram is called a PMF

can find mean and variance using PMF. for mean, simply multiply each unique value by its PMF distribution. for variance do this:
2=i pixi- 2
where the xi are the unique values in the PMF and pi = PMF(xi)

histograms and PMFs are good for exploring data, but might not be best visualization for representing the effect you aim to show

ranges used to group data are called bins

relative risk is a ratio of two probabilities

conditional probability, self-explanatory but interesting term

exercise 8 answers (also in a txt file):
Summary statistics for story on evening news:

    Risks (firsts:others)
    Prob Early: 1.08373628617
    Prob On Time: 0.897311775027
    Prob late: 1.65778116662

    First babies 65% more likely to be late, on time only 90% of the time.

Summary statistics to reassure anxious patient:

    First babies 38.6009517335
    Others 38.5229144667
    Difference in days 0.546260867443

    On average there is only a difference of a half day between first babies and others

Answer: "Do first babies arrive late?"

Pregnancy is a time of hope and excitement for couples and families, but it comes with no shortage of anxiety. One concern many have is over the differences in birth time between a first child as opposed to a second, third or other, later child. Many have the question of whether first babies arrive late.

The answer that first babies are in fact more likely to be late, but not by any amount of time significant to the child's health. First babies are 65% more likely to be late than other births, but the overall difference between the two groups is only 0.54 days.

## Chapter 3 - Cumulative distribution functions
Pmf works well when number of values is small. Actually I had this thought as well, namely that when a lot of values are put in each value’s probability is so small as to be fairly meaningless. The text says “the probability associated with each value gets smaller and the effect of random noise increases”.

this problem can be overcome through binning, but this is difficult. for example, how do we know what size is appropriate for bins? bins that are big enough to smooth out noise may also smooth out useful info

a solution to this is the cumulative distribution function

not sure if this is right, but it seems that a CDF is simply a PMF for which a given value is inclusive of another set of other values. for example, for the percentile of a grade of 70% in a set of grades, the percentile is the probability that a value is 70%, plus the value of the probability of everything below 70. not sure...

CDF is the “area so far” function of the probability distribution

in a uniform distribution, each of a finite number of values is equally likely/probable to be observed

resampling is generating a random sample based on a measured sample

interquartile range is difference between 75th and 25th percentiles
