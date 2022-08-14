import os, sys
path = os.path.dirname('/'.join(os.path.abspath(__file__).split('/')))
sys.path.append(path)

import pandas as pd
import pickle

d = pickle.load(open('/Users/ymdt/src/DREEM_Herschlag/data/H2.p', 'rb'))

for s,q in d['5091'].__dict__.items():
    print('5091')
    print(s,q)

for s,q in d['5092'].__dict__.items():
    print('5092')
    print(s,q)
exit()
