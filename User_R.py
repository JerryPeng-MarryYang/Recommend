import DataSet
import math
import Evaluating


def usersimilarity(train):
    w = dict()
    for u in train.keys():
        w[u] = {}
        for v in train.keys():
            if v not in w[u].keys():
               w[u][v] = 0
            if u == v:
                continue
            w[u][v] = len(train[u] & train[v]) * 1.0
            if w[u][v] != 0:
                w[u][v] /= math.sqrt(len(train[u]) * len(train[v]) * 1.0)
    return w


def usersimilarity_iif(train, pop):

    w = dict()
    for u in train.keys():
        w[u] = {}
        for v in train.keys():
            if v not in w[u].keys():
               w[u][v] = 0
            if u == v:
                continue
            for i in train[u] & train[v]:
                w[u][v] += 1.0 / math.log(1 + pop[i])
    pop = dict()
    for user in train.keys():
        for item in train[user]:
            if item not in pop:
                pop[item] = 0.0
            pop[item] += 1
            if w[u][v] != 0:
                w[u][v] /= math.sqrt(len(train[u]) * len(train[v]) * 1.0)
    return w


def recommend(user, train, w, k, n):
    rvi = 1.0
    rank = dict()
    fileter = train[user]
    for v, wuv in sorted(w[user].items(), key=lambda x: x[1], reverse=True)[0:k]:
        for i in train[v]:
            if i not in fileter:
                if i not in rank.keys():
                    rank[i] = 0.0
                rank[i] += wuv * rvi
    rank = dict(sorted(rank.items(), key=lambda x: x[1], reverse=True)[0:n])
    return rank


dataset = DataSet.openfile('ratings.csv')
train, test = DataSet.splitdata_d(dataset)
pop = DataSet.popu(train)
w = usersimilarity_iif(train, pop)
re = {}
for user in test.keys():
    re[user] = recommend(user, train, w, 60, 10)

x = Evaluating.recall(test, re)
y = Evaluating.precision(test, re)
z = Evaluating.coverage(train, test, re)
a = Evaluating.popularity(pop, re)
print(x)
print(y)
print(z)
print(a)



