import DataSet
import math
import Evaluating


def itemsimliarity(train):
    w = dict()
    n = dict()
    for user, item in train.items():
        for i in item:
            if i not in w.keys():
                w[i] = {}
            if i not in n.keys():
                n[i] = 0
            n[i] += 1
            for j in item:
                if j not in w[i].keys():
                    w[i][j] = 0.0
                if i == j:
                    continue
                w[i][j] += 1.0
    for i in w.keys():
        for j in w[i].keys():
            if w[i][j] != 0.0:
                w[i][j] /= (math.sqrt(n[i] * n[j]) * 1.0)

    return w


'''推荐和用户兴趣列表中的书最相似的k个电影然后返回评分最高的n个电影'''
def recommend(user, train, w, k, n):
    rank = dict()
    rui = 1.0
    fileter = train[user]
    for i in fileter:
        for j, wij in sorted(w[i].items(), key=lambda x: x[1], reverse=True)[0:k]:
            if j in fileter:
                continue
            rank[j] = wij * rui
    rank = dict(sorted(rank.items(), key=lambda x: x[1], reverse=True)[0:n])
    return rank


if __name__ == '__main__':
    dataset = DataSet.openfile('ratings.csv')
    train, test = DataSet.splitdata_d(dataset)
    w = itemsimliarity(train)
    re = {}
    for user in test.keys():
        re[user] = recommend(user, train, w, 10, 10)

    x = Evaluating.recall(test, re)
    y = Evaluating.precision(test, re)
    z = Evaluating.coverage(train, test, re)
    a = Evaluating.popularity(train, re)
    print(x)
    print(y)
    print(z)
    print(a)