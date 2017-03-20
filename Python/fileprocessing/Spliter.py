# -*- coding: utf-8 -*-
"""
Created on Fri Oct 28 11:17:06 2016

@author: mggm6
"""

import pandas as pd
from sklearn.cross_validation import train_test_split

all_data = pd.read_csv('SummaryPh4&6&8.csv')
train, test = train_test_split(all_data, test_size=0.25, random_state=7)
train.to_csv('train.csv')
test.to_csv('test.csv')