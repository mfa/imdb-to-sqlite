import json
import tempfile

import pytest
import sqlite_utils

from imdb_to_sqlite.utils import process_csv


@pytest.fixture
def csv_file():
    data = """Const,Your Rating,Date Rated,Title,URL,Title Type,IMDb Rating,Runtime (mins),Year,Genres,Num Votes,Release Date,Directors
tt1000252,10,2012-01-07,Doctor Who: Blink,https://www.imdb.com/title/tt1000252/,tvEpisode,9.8,45,2007,"Adventure, Drama, Family, Mystery, Sci-Fi",18217,2007-06-09,Hettie Macdonald"""

    with tempfile.NamedTemporaryFile(mode="w") as fp:
        fp.write(data)
        fp.seek(0)
        yield fp.name


def test_process_csv(csv_file):
    db = sqlite_utils.Database(memory=True)
    process_csv(db, csv_file)
    rows = list(db["ratings"].rows)
    assert len(rows) == 1
    assert len(rows[0]) == 15
    assert rows[0]["year"] == 2007
    assert rows[0]["date_rated"] == "2012-01-07"

    # check arrays
    genres = json.loads(rows[0]["genres"])
    assert len(genres) == 5
    assert genres[0] == "Adventure"
    directors = json.loads(rows[0]["directors"])
    assert len(directors) == 1

    # check added fields
    assert rows[0]["year_rated"] == 2012
    assert rows[0]["weekday_rated"] == "Saturday"
