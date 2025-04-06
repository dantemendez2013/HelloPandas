import click
import pandas as pd

@click.command()
@click.argument('csv_file_path', type=click.Path(exists=True))
@click.argument('parquet_file_path', type=click.Path(exists=True))
def cli(csv_file_path: str, parquet_file_path: str):
    print(f'Hello Pandas CSV:\n{pd.read_csv(csv_file_path)}')
    print(f'Hello Pandas Parquet:\n{pd.read_parquet(parquet_file_path)}')

if __name__ == '__main__':
    cli()
