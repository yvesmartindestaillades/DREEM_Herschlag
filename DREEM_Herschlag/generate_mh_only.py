import os

def generate_mh_only_folder(samples):
    if not os.path.exists('mh_only'):
        os.mkdir('mh_only')
    for s in samples:
        if not os.path.exists('mh_only/'+s):
            os.mkdir('mh_only/'+s)
            os.system(f"cp output/{s}/BitVector_Files/mh.p mh_only/{s}/mh.p")
        print(f"transfered mh.p to mh_only/{s}")