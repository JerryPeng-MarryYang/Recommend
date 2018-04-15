import csv
import random


def openfile(filename):
    csvfile = open(filename, 'r')
    r = csv.reader(csvfile)
    l = list(r)[1:]
    return l


def splitdata_l(dataset, m=10, k=0, seed=10, num=2):
    test = []
    train = []
    random.seed(seed)
    for line in dataset:
        if random.randint(0, m-1) == k:
            test.append(line[:num])
        else:
            train.append(line[:num])
    return train, test


def splitdata_d(dataset, m=10, k=0, seed=10):
    test = {}
    train = {}
    random.seed(seed)
    for line in dataset:
        user = line[0]
        if random.randint(0, m-1) == k:
            if user not in test.keys():
                test[user] = set()
            test[user].add(line[1])
        else:
            if user not in train.keys():
                train[user] = set()
            train[user].add(line[1])

    return train, test



if __name__ == '__main__':
    print('This is DataSet File. Pleaser put down your weapons '
          'and put up your hands')



