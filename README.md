## IMDB ratings to sqlite

![Tests](https://github.com/mfa/imdb-to-sqlite/workflows/Tests/badge.svg)

## About

Convert the IMDB ratings CSV file into a sqlite database for easy usage with [Datasette](https://github.com/simonw/datasette).


## Why?

What does this converter different than [csvs-to-sqlite](https://github.com/simonw/csvs-to-sqlite)?

- `genre` and `directors` are array fields
- additional fields for faceting: `year_rated`, `weekday_rated`


## Download data

On the "Your Ratings" page in the "three horizontal dots menu" on top of the table you can download your personal CSV file.


## Install


```
python setup.py install
```


## Convert CSV file

```
imdb-to-sqlite convert imdb-ratings.db imdb-ratings.csv
```


## Use with Datasette

install Datasette:

```
pip install datasette
```

run with Datasette:

```
datasette imdb-ratings.db
```


## Thanks

[Simon Willison](https://simonwillison.net/) for Datasette and sqlite-utils.
