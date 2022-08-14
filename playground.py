import os, sys
path = os.path.dirname('/'.join(os.path.abspath(__file__).split('/')))
sys.path.append(path)

import pandas as pd

df = pd.read_csv('/Users/ymdt/src/dreem_herschlag/data/library.csv')
print(df)

df['name'] = df['name'].astype(str).apply(lambda x: "'{}'".format(x))

print(df)

df.to_csv('/Users/ymdt/src/dreem_herschlag/data/library.csv', index=False)