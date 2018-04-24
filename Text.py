import DataSet

dataset = DataSet.openfile('ratings.csv')
train, test = DataSet.splitdata_d(dataset)

s = {'593', '356'}
n = 0
for x in train.values():
    if s.issubset(x):
        n += 1
print(n)