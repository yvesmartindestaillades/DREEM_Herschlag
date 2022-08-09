## Herschlag lab DREEM DREEM_Herschlag

This repo is a wrapper for Joe Yesselman's DREEM module, that implements the DREEM algorithm developed by the Rouskin lab.

The wrapper allows the user to run DREEM on different samples and to add standardized experimental details to DREEM output.


## Installation

DREEM_Herschlag is available on PyPi:

```
pip install dreem_herschlag
```

You can also clone this repo and run make:

```
cd [PATH_TO_WHERE_YOU_WANT_THE_REPO]
git clone https://github.com/yvesmartindestaillades/DREEM_Herschlag
cd DREEM_Herschlag
make init
```

## Run DREEM

### Write additional experimental information files 

To add additional experimental information to DREEM's output, you will have to fill in two different types of files, samples.csv and library.csv.

`samples.csv` contains information about the sample as a whole, such as the temperature or the date. 
Each row of `samples.csv` correspond to a single sample. 
The `sample` column of `samples.csv` must match the folders names.

Columns description for `samples.csv` can be found by typing:

```
dreem_herschlag --print_sample
```

### Organize your sequencing files
Your fasta/fastq files organization should look like this:
```
|- /[path_to_data]
     |- samples.csv
     |- /[your_sample_1]
          |- r1.fastq
          |- r2.fastq
          |- ref.fasta
          |- library.csv
     |- /[your_sample_2]
          |- ...
     |- /[your_sample_3]
          |- ...
```
Don't forget to include `samples.csv` at the root of `path_to_data` and library.csv in each sample folder.

### Fill in config.yml

- Download the `config-template.yml` template at the root of this repo.
- Follow the instructions to fill the template.

> **_NOTE:_** your folders and fasta/fastq files must have specific names and be in 
