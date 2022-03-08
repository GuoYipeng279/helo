import pandas as pd
import os
for i,j,k in os.walk('xls'):
    pass
dfs = []
cons = []
for i in k:
    df = pd.read_excel('xls\\'+i,header=2)
    dfs.append(df[4:37])
    dfs[-1] = dfs[-1].rename(columns={'Partner country':'partner'})
    cons.append(list(dfs[-1].columns)[2])

import numpy as np
matr = np.zeros((39,39))
index_dict = dict()
for i,j in enumerate(cons):
    index_dict[j] = i
for con, df in zip(cons,dfs):
    for partner in cons:
        query = np.array(df.query("partner == '{}'".format(partner)))
        print(query)
        qq = 0. if len(query)==0 or query[0][2]=='..' else query[0][2]
        matr[index_dict.get(con), index_dict.get(partner)] = qq

from matplotlib import pyplot as plt
plt.imshow(np.log(matr),cmap='gray')
plt.show()