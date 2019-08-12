#### IMPORTS ####
import numpy as np
import pandas as pd


#### THE DATA ####
train = pd.read_csv('mitbih_train.csv', header=None)
test = pd.read_csv('mitbih_test.csv', header=None)

normal_data = pd.read_csv('ptbdb_normal.csv', header=None)
abnormal_data = pd.read_csv('ptbdb_abnormal.csv', header=None)

merged_mit = pd.concat([train, test])
merged_ptb = pd.concat([normal_data, abnormal_data])

print(train.shape, test.shape, merged_mit.shape)
print(normal_data.shape, abnormal_data.shape, merged_ptb.shape)

print(merged_mit[187].value_counts())
print(merged_ptb[187].value_counts())
