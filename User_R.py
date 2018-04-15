import DataSet
import math
import Evaluating


def usersimilarity(train):
    w = dict()
    for u in train.keys():
        w[u] = {}
        for v in train.keys():
            if u == v:
                continue
            w[u][v] = len(train[u] & train[v]) * 1.0
            if w[u][v] != 0:
                w[u][v] /= math.sqrt(len(train[u]) * len(train[v]) * 1.0)
    return w


def recommend(user, train, w, k, n):
    rvi = 1.0
    rank = dict()
    fileter = train[user]
    for v, wuv in sorted(w[user].items(), key=lambda x: x[1], reverse=True)[0:k]:
        #print(v, wuv)
        for i in train[v]:
            if i not in fileter:
                if i not in rank.keys():
                    rank[i] = 0.0
                rank[i] += wuv * rvi
    rank = dict(sorted(rank.items(), key=lambda x: x[1], reverse=True)[0:n])
    return rank


dataset = DataSet.openfile('ratings.csv')
train, test = DataSet.splitdata_d(dataset)
w = usersimilarity(train)
re = {}
for user in test.keys():
    re[user] = recommend(user, train, w, 5, 10)

x = Evaluating.recall(test, re)
y = Evaluating.precision(test, re)
print(x)
print(y)




'''for line in re.items():
    print(line)
r = recommend('2', train, w, 10)
print(len(r))
for line in sorted(r.items(), key=lambda x: x[1], reverse=True):
    print(line)'''


