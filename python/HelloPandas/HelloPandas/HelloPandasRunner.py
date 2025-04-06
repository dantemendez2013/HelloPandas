import click
import pandas as pd

@click.command()
@click.argument('csv_file_path', type=click.Path(exists=True))
def cli(csv_file_path: str):
    print(f'Hello Pandas:\n{pd.read_csv(csv_file_path)}')

if __name__ == '__main__':
    cli()
