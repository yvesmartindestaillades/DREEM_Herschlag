#!/usr/bin/env python3
# # USER EDIT PARAMETERS HERE
####################################################################


####################################################################


## SANITY CHECKS
####################################################################



## RUN 
####################################################################

from dreem import util

## TO REMOVE
print(util.run_command('pip3 install .')[0])


for s in SAMPLES_TO_PROCESS:
    cmd = 'dreem'
    for fast_arg, fast_file in zip(['-fq1','-fq2','-fa','--library_info'],FILES_PER_SAMPLE):
        cmd += ' '+fast_arg+' '+PATH_TO_DATA+f"{s}/"+fast_file
    for key, val in dreem_args.items():
        if (not (type(val) == bool)) or val:
            cmd += ' '+ key + ' '+ (val if type(val) != bool else '')
    cmd += ' --sample '+s
    if VERBOSE: print(cmd)
    print(util.run_command(cmd)[0]) if VERBOSE else util.run_command(cmd)

## TO REMOVE
print(util.run_command('/Library/Frameworks/Python.framework/Versions/3.10/bin/python3.10 /Users/ymdt/src/dreem/my_test_zone.py')[0])
