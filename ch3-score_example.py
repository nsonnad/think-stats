scores = [55, 66, 77, 88, 99]

def PercentileRank(numbers, a_score):
    count = 0
    for score in scores:
        if score <= a_score:
            count += 1

    percentile_rank = 100.0 * count / len(scores)
    return percentile_rank


print 'score, percentile rank'
for score in scores:
    print score, PercentileRank(scores, score)


def Percentile(numbers, a_percentile):
    numbers.sort()
    index = a_percentile * (len(scores) - 1) / 100
    return numbers[index]


# def Selection_Algorithm(numbers, a_percentile):
#     count = 0
#     nums = [i for i in numbers if i <= ]
#         if /len(numbers) <= a_percentile:
#             count += 1

#     percentile =


print 'prank, score'
for percentile_rank in [0, 20, 25, 40, 50, 60, 75, 80, 100]:
    print percentile_rank, Percentile(scores, percentile_rank)