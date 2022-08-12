import pickle
import pandas as pd

class AddInfo(object):
    def __init__(self, config) -> None:
        self.samples = config['samples']
        self.config = config

    def load_pickle(self, path):
        pass

    def save_pickle(self, path, obj):
        pass

    def load_samples(self, s):
        pass

    def load_library(self, path):
        pass
    
    def run(self):
        if not self.config['skip_samples']:
            df_samp = pd.read_csv(self.config['path_to_data']+'/samples.csv')
        if not self.config['skip_library']:
            df_lib = pd.read_csv(self.config['path_to_data']+'/library.csv')
        for s in self.samples:
            self.config['add_info'] = self.config['add_info']+'/' if self.config['add_info'][-1]!= '/' else self.config['add_info']
            pf = pickle.load(open(self.config['add_info'] + s +'.p', 'rb'))
            for name, mh in pf.items():
                if not self.config['skip_samples']:
                    for col in df_samp.columns:
                        assert (data:=df_samp[col].loc[df_samp['sample']==s] is not None), f"{s} doesn't have {col} in samples.csv"
                        setattr(mh,col,data)
                if not self.config['skip_library']:
                    for col in df_lib.columns:
                        assert(data :=df_lib[col].loc[df_lib['name']==name]) is not None, f"{name} not found in library.csv for col {col}"
                        setattr(mh,col,data)
            pickle.dump(pf, open(self.config['add_info'] + s +'.p', 'wb'))