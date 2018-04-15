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
