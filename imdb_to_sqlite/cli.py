import click
import sqlite_utils

from imdb_to_sqlite.utils import process_csv


@click.group()
@click.version_option()
def cli():
    "Convert IMDB ratings CSV to a SQLite database"


@cli.command()
@click.argument(
    "db_path",
    type=click.Path(file_okay=True, dir_okay=False, allow_dash=False),
    required=True,
)
@click.argument(
    "csv_path",
    type=click.Path(file_okay=True, dir_okay=False, allow_dash=False),
    default="imdb-ratings.csv",
)
def convert(db_path, csv_path):
    db = sqlite_utils.Database(db_path)
    process_csv(db, csv_path)
