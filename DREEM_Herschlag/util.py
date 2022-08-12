
from DREEM_Herschlag.resources import __file__ as resources_file
from DREEM_Herschlag import __file__ as DREEM_Herschlag_file
import yaml, os, subprocess

class Path(object):
    def __init__(self) -> None:    
        self.resources_file = '/'.join(resources_file.split('/')[:-1])
        self.DREEM_Herschlag_file = '/'.join(DREEM_Herschlag_file.split('/')[:-1])
        self.sample_attribute_path = self.resources_file+'/sample_attributes.yml'
        self.library_attributes_path = self.resources_file+'/library_attributes.yml'
        self.config_template = self.resources_file+'/config-template.yml'

def run_command(cmd):
    output, error_msg = None, None
    try:
        output = subprocess.check_output(
                cmd, shell=True, stderr=subprocess.STDOUT
        ).decode("utf8")
    except subprocess.CalledProcessError as exc:
        error_msg = exc.output.decode("utf8")
    return output, error_msg

def format_path(path):
    if path == '.':
        path = os.path.abspath('')
    if path[-1] != '/':
        path = path+'/'
    if not os.path.exists(path):
        os.makedirs(path)
    return path

def generate_mh_only_folder(samples):
    if not os.path.exists('mh_only'):
        os.mkdir('mh_only')
    for s in samples:
        if not os.path.exists('mh_only/'+s):
            os.mkdir('mh_only/'+s)
            os.system(f"cp output/{s}/BitVector_Files/mh.p mh_only/{s}/mh.p")
        print(f"transfered mh.p to mh_only/{s}")