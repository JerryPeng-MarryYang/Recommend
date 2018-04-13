import csv
import random


def openfile(filename):
    csvfile = open(filename, 'r')
    r = csv.reader(csvfile)
    l = list(r)[1:]
    return l


def splitdata(dataset, m=10, k=0, seed=10, num=2):
    test = {}
    train = {}
    random.seed(seed)
    for line in dataset:
        user = line[0]
        if random.randint(0, m-1) == k:
            test.append(line[:num])
        else:
            train.append(line[:num])
    return train, test


if __name__ == '__main__':
    dataset = openfile('ratings.csv')
    train, test = splitdata(dataset)
    print(len(train))
    print(len(test))


