import click
from click_option_group import optgroup
import yaml
from DREEM_Herschlag.sanity_check import Sanity_check

@click.command()
@optgroup.group("main arguments")
@optgroup.option("-c", "--config", type=click.Path(exists=True), required=True,
                 help="reference sequences in fasta format")

def main(**args):
    """
    DREEM processes DMS next generation sequencing data to produce mutational
    profiles that relate to DMS modification rates written by Silvi Rouskin and the
    Rouskin lab (https://www.rouskinlab.com/)
    """
    run(args)


def run(args):
    with open(args['config'], 'r') as f:
        config = yaml.safe_load(f)
    assert config['samples'], "No samples found in config file"
    assert config['files_per_sample'], "No files_per_sample found in config file"
    assert config['path_to_data'], "No path_to_data found in config file"
    assert config['dreem_args'], "No dreem_args found in config file"
    assert config['verbose'], "No verbose found in config file"
    assert config['sample_file'], "No sample_file found in config file"

    Sanity_check(config).run()
    print("Sanity check passed")

    


if __name__ == "__main__":
    main()
