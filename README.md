# Welcome to the Herschlag lab's wrapper for DREEM

This repo is a wrapper for [Joe Yesselman's DREEM module](https://github.com/jyesselm/dreem), that implements the DREEM algorithm developed by the Rouskin lab.

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

### Organize your sequencing files
Your fasta/fastq files organization should look like this:

```
|- /path/to/data
     |- samples.csv
     |- /your_sample_1
          |- r1.fastq
          |- r2.fastq
          |- ref.fasta
          |- library.csv
     |- /your_sample_2
          |- ...
     |- /your_sample_3
          |- ...
```

### Write additional experimental information files (optional)

To add additional experimental information to DREEM's output, you can to create two different types of files, samples.csv and library.csv.

Generate templates for `samples.csv`, `library.csv` and `my_config.yml` by running:

```
dreem_herschlag --generate_templates
```

`samples.csv` contains information about the sample as a whole, such as the temperature or the date. 
Each row of `samples.csv` correspond to a single sample. 
The `sample` column of `samples.csv` must match the `your_sample_#` folders names shown above.

Columns description for `samples.csv` can be found by typing:

```
dreem_herschlag --sample_info
```

> __*NOTE:*__ `exp_env` MUST BE `in_vivo` or `in_vitro`, or the code won't run

`library.csv` contains information about each construct in a sample.
There must be one `library.csv` file per sample.
The `name` column of `library.csv` should match the constructs name of the fasta file.

Columns description for `library.csv` can be found by typing:

```
dreem_herschlag --library_info
```

### Fill in config.yml

- Download the `template_config.yml` template at the root of this repo, or generate it with ``dreem_herschlag --generate_templates``
- You may rename your file `my_config.yml` or whatever sounds good to you, so that you don't overwrite it.
- Open the file and follow the fill-in instructions.

### RUN!

```
dreem_herschlag --config my_config.yml
```


Thanks for reading. 
Please contact me at yves@martin.yt for any additional information or to contribute.
