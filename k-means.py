import DataSet
from pandas import DataFrame
import numpy as np
dataset = DataSet.openfile('ratings.csv')
train, test = DataSet.splitdata_d(dataset)
user = set()
movie = set()
for u, item in train.items():
    user.add(u)
    for m in item:
        movie.add(m)
matric = DataFrame(index=movie, columns=user,)

for u, item in train.items():
    for m in item:
        matric.loc[m][u] = 1.0
matric.fillna(0.0, inplace=True)

def distance(x, y):
    return np.sqrt(np.sum(np.square(x - y)))

def kmeans(matric=matric, n=3, fn=100):
    l = matric.columns
    ans = {}
    preans = {}
    for i in range(n):
        if i not in ans:
            ans[i] = DataFrame(columns=l)
            ans[i].loc[matric.iloc[i].name] = matric.iloc[i]
    iii = 0
    while iii < fn & (preans != ans):
        preans = ans
        for m in movie:
            inde = '0'
            min = 10000.0
            x = matric.loc[m]
            for i in range(n):
                d = distance(x, ans[i].iloc[0])
                if d < min:
                    min = d
                    inde = i
            ans[inde].loc[m] = x
        for i in range(n):
            tem = ans[i].mean()
            tem.name = 0
            if iii != fn - 1 & (preans != ans):
                ans[i].drop(ans[i].index, inplace=True)
            ans[i].loc[tem.name] = tem
        iii += 1
    return ans


if __name__ == '__main__':
    #f = open('a.txt', 'w')
    #print(matric)
    ans = kmeans()
    for line in ans.values():
        print(line)#, file=f)
