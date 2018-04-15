import math


def recall(test, recommend):
    hit = 0
    all = 0
    for i in test.keys():
        hit += len(set(recommend[i].keys()) & test[i])
        all += len(test[i])
    return hit / (all * 1.0)


def precision(test, recommend):
    hit = 0
    all = 0
    for i in test.keys():
        hit += len(set(recommend[i].keys()) & test[i])
        all += len(recommend[i].keys())
    return hit / (all * 1.0)


def coverage(train, test, recommend):
    all = set()
    re = set()
    for user in train.keys():
        all = all | (train[user])
    for user in test.keys():
        all = all | (test[user])
    for user in recommend.keys():
        re = re | set(recommend[user].keys())

    return len(re) / (len(all) * 1.0)


def popularity(pop, recommend):
    # pop = dict()
    # for user in train.keys():
    #     for item in train[user]:
    #         if item not in pop:
    #             pop[item] = 0.0
    #         pop[item] += 1

    ret = 0
    n = 0

    for user in recommend.keys():
        for item in recommend[user].keys():
            ret = math.log(1 + pop[item])
            n += 1

    ret /= (n * 1.0)
    return ret