from sqlalchemy import create_engine, Table, Column, String, Integer
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import csv

def main():
    engine = create_engine("postgres://postgres:1234@localhost:5432/pr1", echo=True)
    db = scoped_session(sessionmaker(bind=engine))
    drop_table_if_exists(db)
    create_books_table(db)
    insert_books(db)
    print_books_from_db(db)


def drop_table_if_exists(db):
    db.execute("DROP TABLE IF EXISTS tbl_book")
    db.commit()


def create_books_table(db):
    db.execute("CREATE TABLE tbl_book(isbn TEXT PRIMARY KEY,"\
                                      "title TEXT NOT NULL,"\
                                      "author TEXT NOT NULL,"\
                                      "year TEXT NOT NULL"\
                                      ")")
    db.commit()


def insert_books(db):
    with open("books.csv","r") as file:
        reader = csv.reader(file)
        list_dict = []

        for isbn, title, author, year in reader:
            list_dict.append({"isbn": isbn, "title": title, "author": author, "year": year})

        db.execute("INSERT INTO tbl_book VALUES(:isbn, :title, :author, :year)", list_dict)
        db.commit()


def print_books_from_db(db):
    res = db.execute("SELECT * FROM tbl_book")

    for isbn, title, author, year in res:
        print(isbn, title, author, year)


if __name__ == '__main__':
    main()
