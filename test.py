
import  pandas as pd
import numpy as np
import os
from pandas import DataFrame,Series
import re
AS =pd.read_csv(r'C:\Users\perlicue\Documents\WeChat Files\wxid_l70ra3lzzmkd22\FileStorage\MsgAttach\c4189b07e8032d81b6f68072eb6f5e98\File\2022-06\offseason_merch.csv')
# print(df.columns)  #查看列名
# print(df.dtypes)
for i in range(1,AS['coupon_disc'].shape[0]):
    if AS['coupon_disc'][i]=='None':
        AS['coupon_disc'][i]=0
coupon_disc = AS['coupon_disc'].astype('float64')
print(AS['coupon_disc'].dtype)

