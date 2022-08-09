import click
from click_option_group import optgroup
import yaml
from DREEM_Herschlag.sanity_check import Sanity_check
from DREEM_Herschlag.run_dreem import Run_dreem
import os

from DREEM_Herschlag.util import echo_attributes_library, echo_attributes_samples

@click.command()
@optgroup.group("main arguments")
@optgroup.option("-c", "--config", type=click.Path(exists=True),
                 help="reference sequences in fasta format")

@optgroup.option("--samples_info", is_flag=True, help="Print the mandatory and optional columns for samples.csv")
@optgroup.option("--library_info", is_flag=True, help="Print the mandatory and optional columns for library.csv")

def main(**args):
    """
    DREEM processes DMS next generation sequencing data to produce mutational
    profiles that relate to DMS modification rates written by Silvi Rouskin and the
    Rouskin lab (https://www.rouskinlab.com/)
    """
    run(args)


def run(args):
    if args['samples_info']:
        echo_attributes_samples()
        exit()
    if args['library_info']:
        echo_attributes_library()
        exit()
    else:
        with open(args['config'], 'r') as f:
            config = yaml.safe_load(f)
        assert config['samples'], "No samples found in config file"
        assert config['files_per_sample'], "No files_per_sample found in config file"
        assert config['path_to_data'], "No path_to_data found in config file"
        assert config['dreem_args'], "No dreem_args found in config file"
        assert config['verbose'], "No verbose found in config file"

        for repo in ['temp', 'output','log','input']:
            if not os.path.exists(repo):
                os.makedirs(repo)
        
        Sanity_check(config).run()
        
        Run_dreem(config).run()
    

if __name__ == "__main__":
    main()
