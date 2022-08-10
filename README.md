# Welcome to the Herschlag lab's wrapper for DREEM

This repo is a wrapper for [Joe Yesselman's DREEM module](https://github.com/jyesselm/dreem), that implements the DREEM algorithm developed by the Rouskin lab.

The wrapper allows the user to run DREEM on different samples and to add standardized experimental details to DREEM output.

## Requirements

DREEM package must be in your environment.
You need RNAstructure installed to run RNAstructure, otherwise deactivate this option in the config file.

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

## Test your installation

Run:

```
cd PATH/TO/REPO
dreem_herschlag --config test/test_config.yml
```

You should get this output:
```
dreem_herschlag --config test/test_config.yml
Checking files
Checking test/resources/samples.csv
Checking samples.csv done

Checking case_1/library.csv
Ignored sequence, not in library_attributes
Checking case_1/library.csv done

Checking files done

Running DREEM
dreem -fq1 test/resources/case_1/r1.fastq -fq2 test/resources/case_1/r2.fastq -fa test/resources/case_1/ref.fasta --sample case_1 --sample_info temp/samples.csv --library_info temp/case_1/library.csv --bootstrap 
[19:12 bit_vector.py run] INFO ran at commandline as: 
[19:12 bit_vector.py run] INFO /Users/ymdt/src/DREEM_Herschlag/bin/dreem -fq1 test/resources/case_1/r1.fastq -fq2 test/resources/case_1/r2.fastq -fa test/resources/case_1/ref.fasta --sample case_1 --sample_info temp/samples.csv --library_info temp/case_1/library.csv --bootstrap
[19:12 bit_vector.py validate_files] INFO fasta file: test/resources/case_1/ref.fasta exists
[19:12 bit_vector.py validate_files] INFO fastq file: test/resources/case_1/r1.fastq exists
[19:12 bit_vector.py validate_files] INFO fastq2 file: test/resources/case_1/r2.fastq exists
[19:12 bit_vector.py validate_files] INFO two fastq files supplied, thus assuming paired reads
[19:12 bit_vector.py build_directories] INFO building directory structure
[19:12 mapper.py __init__] INFO bowtie2 2.4.5 detected!
[19:12 mapper.py __init__] INFO fastqc v0.11.9 detected!
[19:12 mapper.py __init__] INFO trim_galore 0.6.6 detected!
[19:12 mapper.py __init__] INFO cutapt 1.18 detected!
[19:12 mapper.py __skip_without_overwrite] INFO SKIPPING fastqc, it has been run already! specify -overwrite to rerun
[19:12 mapper.py __skip_without_overwrite] INFO SKIPPING trim_galore, it has been run already! specify -overwrite to rerun
[19:12 mapper.py __skip_without_overwrite] INFO SKIPPING bowtie-build, it has been run already! specify -overwrite to rerun
[19:12 mapper.py __skip_without_overwrite] INFO SKIPPING bowtie2 alignment, it has been run already! specify -overwrite to rerun
[19:12 mapper.py __skip_without_overwrite] INFO SKIPPING picard BAM conversion, it has been run already! specify -overwrite to rerun
[19:12 mapper.py __skip_without_overwrite] INFO SKIPPING picard BAM sort, it has been run already! specify -overwrite to rerun
[19:12 mapper.py run] INFO finished mapping!
[19:12 bit_vector.py run] INFO starting bitvector generation
[19:12 bit_vector.py __run_picard_sam_convert] INFO SKIPPING picard SAM convert, it has been run already! specify -overwrite to rerun
[19:12 bit_vector.py __generate_all_bit_vectors] INFO SKIPPING bit vector generation, it has run already! specify -overwrite to rerun
[19:12 bit_vector.py run] INFO MUTATION SUMMARY:
| name          |   reads |   aligned |   no_mut |   1_mut |   2_mut |   3_mut |   3plus_mut |   sn |
|---------------|---------|-----------|----------|---------|---------|---------|-------------|------|
| mttr-6-alt-h3 |    2332 |     99.96 |    46.42 |   36.81 |   13.21 |    3.05 |        0.04 | 7.76 |

None
DREEM done
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
