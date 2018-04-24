import pandas as pd
import DataSet
from pandas import DataFrame
import sys
from collections import defaultdict

dataset = DataSet.openfile('ratings.csv')
train, test = DataSet.splitdata_d(dataset)
pop = dict()
for user in train.keys():
    for item in train[user]:
        if item not in pop:
            pop[item] = 0.0
        pop[item] += 1
# print(list((id, num) for id, num in pop.items() if num > 50))

def find_frequent_set(train, lastset, min_support):
    counts = defaultdict(int)
    tag = defaultdict(int)
    for reviews in train.values():
        tag = defaultdict(int)
        for itemset in lastset:
            if itemset.issubset(reviews):
                for othermovie in reviews - itemset:
                    current_super_set = itemset | frozenset((othermovie,))
                    #print(tag[current_super_set])
                    # counts[current_super_set] += 1
                    if not tag[current_super_set]:
                        counts[current_super_set] += 1
                        tag[current_super_set] = True
    return dict([(itemset, frequency) for itemset, frequency in counts.items() if frequency >= min_support])


frequent_itemsets = {}
min_support = 90
frequent_itemsets[1] = dict((frozenset((movieid,)), num) for movieid, num in pop.items() if num > min_support)
print('find {0} frequent sets {1}'.format(1, len(frequent_itemsets[1])))
print('They are:')
print(frequent_itemsets[1])

max_length = 20
for k in range(2, max_length):
    cur_frequent_itemsets = find_frequent_set(train, frequent_itemsets[k - 1], min_support)
    if len(cur_frequent_itemsets) == 0:
        print('no frequent set')
        break
    else:
        print('find {0} frequent sets {1}'.format(k, len(cur_frequent_itemsets)))
        print('They are:')
        print(cur_frequent_itemsets)
        frequent_itemsets[k] = cur_frequent_itemsets


k = len(frequent_itemsets)
print(k)
print(frequent_itemsets[k])
min_conf = 0.0
candidate_rules = defaultdict(float)

for itemset, num in frequent_itemsets[k].items():
    for x, cur_frequent_itemsets in frequent_itemsets.items():
        if x == 4:
            continue
        for it, n in cur_frequent_itemsets.items():
            conf = num * 1.0 / n
            if  conf >= min_conf:
                if it.issubset(itemset):
                    conclusion = itemset - it
                    candidate_rules[(it, conclusion)] = conf
print(candidate_rules)


