
from setuptools import setup, find_packages
import os, sys
from DREEM_Herschlag import __version__
from DREEM_Herschlag.util import Path
import sys

path = Path()

try:
    with open('requirements.txt') as f:
        requirements = f.read().splitlines()
except:
    try:
        with open('../requirements.txt') as f:
            requirements = f.read().splitlines()

    except:
        try:
            with open(path.root_file+'/requirements.txt') as f:
                requirements = f.read().splitlines()
        except:
            raise(Exception('requirements.txt not found'))

PYTHON_VERSION = (3,10)

if sys.version_info < PYTHON_VERSION:
    sys.exit(f"Python >= {PYTHON_VERSION[0]}.{PYTHON_VERSION[1]} required.")


setup(
   name='DREEM_Herschlag',
   version=__version__,
   license="MIT",
   description='A wrapper for DREEM for the Herschlag lab',
   author='Yves Martin des Taillades',
   author_email='yves@martin.yt',
   long_description= 'TODO',
#   packages=['DREEM_Herschlag'],
   packages=find_packages(),  #+['DREEM_Herschlag'],
   package_data={'': ['*.yml']},
   package_dir={'DREEM_Herschlag': 'DREEM_Herschlag'},
   py_modules=[
       'DREEM_Herschlag/sanity_check',
       'DREEM_Herschlag/run_dreem',
       'DREEM_Herschlag/run',
       'DREEM_Herschlag/util',
   ],
   include_package_data=True,
   install_requires=requirements, #external packages as dependencies
    entry_points = {
        'console_scripts' : [
            'dreem_herschlag = DREEM_Herschlag.run : main'
        ]
    },
    url='https://github.com/yvesmartindestaillades/DREEM_Herschlag',

)
