import DataSet
import math
import Evaluating
import os


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


def usersimilarity_iif(train):

    pop = dict()
    for user in train.keys():
        for item in train[user]:
            if item not in pop:
                pop[item] = 0.0
            pop[item] += 1

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
    # pop = dict()
    # for user in train.keys():
    #     for item in train[user]:
    #         if item not in pop:
    #             pop[item] = 0.0
    #         pop[item] += 1
            if w[u][v] != 0:
                w[u][v] /= math.sqrt(len(train[u]) * len(train[v]) * 1.0)
    return w


#'''推荐和用户最相近的k个用户的电影从中选取n个评分最高的返回'''
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
w = usersimilarity_iif(train)
w1 = usersimilarity(train)

re = {}
re1 = {}
for user in test.keys():
    re[user] = recommend(user, train, w, 16, 16)
    re1[user] = recommend(user, train, w1, 16, 16)

x = Evaluating.recall(test, re)
y = Evaluating.precision(test, re)
z = Evaluating.coverage(train, test, re)
a = Evaluating.popularity(train, re)


x1 = Evaluating.recall(test, re1)
y1 = Evaluating.precision(test, re1)
z1 = Evaluating.coverage(train, test, re1)
a1 = Evaluating.popularity(train, re1)


# print('%.5f' % x, ',', '%.5f' % y, ',', '%.5f' % z, ',', '%.5f' % a)
# print('%.5f' % x1, ',', '%.5f' % y1, ',', '%.5f' % z1, ',', '%.5f' % a1)
filename = 'b.txt'
if os.path.exists(filename):
    os.remove(filename)
file = open(filename, 'a')

print('recall,precision,coverage,popularity', file=file)
print(x, ',', y, ',', z, ',', a, file=file)
print(x1, ',', y1, ',', z1, ',', a1, file=file)


#
# filename = 'a.txt'
# if os.path.exists(filename):
#     os.remove(filename)
# file = open(filename, 'a')
# for n in range(2, 100, 2):
#     re = {}
#     for user in test.keys():
#         re[user] = recommend(user, train, w, 16, n)
#
#     x = Evaluating.recall(test, re)
#     y = Evaluating.precision(test, re)
#     z = Evaluating.coverage(train, test, re)
#     a = Evaluating.popularity(train, re)
#     print(n, ',', '%.5f' % x, ',', '%.5f' % y, ',', '%.5f' % z, ',', '%.5f' % a, file=file)
#     file.flush()
#



