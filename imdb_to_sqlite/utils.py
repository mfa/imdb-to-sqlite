import csv
import datetime


def create_table(db):
    if not db["ratings"].exists():
        db["ratings"].create(
            {
                "pk": str,
                "title": str,
                "your_rating": int,
                "imdb_rating": float,
                "date_rated": str,
                "year": int,
                "title_type": str,
                "runtime_mins": int,
                "genres": str,  # used as array
                "num_votes": int,
                "release_date": str,
                "directors": str,  # used as array
                "url": str,
                # additional columns for faceting
                "year_rated": int,
                "weekday_rated": str,
            },
            pk="pk",
        )


def preprocess_dataset(row):
    d = {}
    for key, value in row.items():
        if key == "Const":
            d["pk"] = value
            continue
        _key = key.lower().replace(" ", "_").replace("(", "").replace(")", "")
        if key in ["Genres", "Directors"]:
            value = value.split(", ")
        d[_key] = value

    date_rated = datetime.datetime.strptime(d["date_rated"], "%Y-%m-%d").date()
    d["year_rated"] = date_rated.year
    d["weekday_rated"] = date_rated.strftime("%A")
    return d


def process_csv(db, csv_path):
    create_table(db)
    with open(csv_path, newline="", encoding="latin1") as csvfile:
        reader = csv.DictReader(csvfile)
        db["ratings"].insert_all(
            ([preprocess_dataset(row) for row in reader]),
            replace=True,
            batch_size=1000,
        )
