#!/usr/bin/env python

import click
import seaborn as sns

@click.command()
@click.option('--dataset', default='healthexp', help='Name of the dataset – github.com/mwaskom/seaborn-data')
@click.version_option(version='1.2.0')
def main(dataset):
    """
    A demo App2 for BIOS259: The Art of Reproducible Science
    https://github.com/asntech/bios259-a24
    
    Author: Aziz Khan <azizk@stanford.edu>
    """
    # Load the dataset
    try:
        dataset = sns.load_dataset(dataset)
    except ValueError as e:
        click.echo(f"Error: {e}")
        return
    
    # Print dataset information
    click.echo(f"Descriptive Statistics for {dataset} dataset:")
    click.echo("==============================================")
    click.echo(dataset.describe())

if __name__ == "__main__":
    main()
