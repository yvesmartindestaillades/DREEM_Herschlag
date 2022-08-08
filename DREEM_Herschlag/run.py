import click
from click_option_group import optgroup


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
    print("hello world")
    print(args)


if __name__ == "__main__":
    main()
