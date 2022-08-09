from pkg_resources import Requirement
from setuptools import setup, find_packages
import os, sys
from DREEM_Herschlag import __version__
import DREEM_Herschlag
import sys

try:
    with open('requirements.txt') as f:
        requirements = f.read().splitlines()
except:
    with open('../requirements.txt') as f:
        requirements = f.read().splitlines()

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
 #  packages=['DREEM_Herschlag'],  #same as name
 #  package_dir={'DREEM_Herschlag': 'DREEM_Herschlag'},
   packages=find_packages(),
   package_data={'': ['*.yml']},
   py_modules=[
       'DREEM_Herschlag/sanity_check',
       'DREEM_Herschlag/run_dreem',
       'DREEM_Herschlag/run',
   ],
   include_package_data=True,
   install_requires=requirements, #external packages as dependencies
    entry_points = {
        'console_scripts' : [
            'dreem_herschlag = DREEM_Herschlag.run : main'
        ]
    }
)