
from DREEM_Herschlag.resources import __file__ as resources_file
from DREEM_Herschlag import __file__ as DREEM_Herschlag_file


class Path(object):
    def __init__(self) -> None:    
        self.resources_file = '/'.join(resources_file.split('/')[:-1])
        self.DREEM_Herschlag_file = '/'.join(DREEM_Herschlag_file.split('/')[:-1])
        self.sample_attribute_path = self.resources_file+'/sample_attributes.yml'
        self.library_attributes_path = self.resources_file+'/library_attributes.yml'

def get_attributes(file):
    path = Path()
    if file == 'samples.csv':
        with open(path.sample_attribute_path, 'r') as f:
            attributes = f.read()
        f.close()

    if file == 'library.csv':
        with open(path.library_attributes_path, 'r') as f:
            attributes = f.read()
        f.close()
    return attributes

def echo_attributes(file):
    attributes = get_attributes(file)
    print(attributes)

def echo_attributes_samples():
    echo_attributes('samples.csv')

def echo_attributes_library():
    echo_attributes('library.csv')
