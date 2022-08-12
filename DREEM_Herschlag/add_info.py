import pickle

class AddInfo(object):
    def __init__(self, config) -> None:
        self.samples = config['samples']

    def load_pickle(self, path):
        pass

    def save_pickle(self, path, obj):
        pass

    def load_samples(self, path):
        pass

    def load_library(self, path):
        pass
    
    def run(self):
        for s in self.samples:
            
        
