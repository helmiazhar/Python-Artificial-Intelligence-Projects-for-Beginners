# -*- coding: utf-8 -*-
"""
Created on Tue Apr  6 18:02:37 2021

@author: Aditya Luthfi
"""

import pandas
from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_extraction.text import CountVectorizer


def preparation():
    dfs = pandas.read_csv('Chapter01/dataset/imdb.csv', sep= ',')

    
    cv = CountVectorizer()
    dfs = dfs.sample(frac=1)
    dfs_train = dfs[:3000]
    dfs_test = dfs[3000:]
    dfs_train_attribute = cv.fit_transform(dfs_train['text'])
    dfs_train_win = dfs_train['label']
    dfs_test_attribute = cv.transform(dfs_test['text'])
    dfs_test_win = dfs_test['label']
    data = [[dfs_train_attribute,dfs_train_win], [dfs_test_attribute, dfs_test_win]]
    return data

def training(dfs_train_att, dfs_train_win):
    t = RandomForestClassifier(n_estimators=100)
    t = t.fit(dfs_train_att,dfs_train_win)
    return t

def testing(t, testdataframe):
    return t.predict(testdataframe)