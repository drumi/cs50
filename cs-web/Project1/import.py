from sqlalchemy import create_engine, Table, Column, String, Integer
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import csv

def main():
    engine = create_engine("postgres://postgres:1234@localhost:5432/pr1", echo=True)
    db = scoped_session(sessionmaker(bind=engine))
    drop_table_if_exists(db)
    create_authors_table(db)
    create_books_table(db)
    insert_books(db)
    print_books_from_db(db)


def drop_table_if_exists(db):
    db.execute("DROP TABLE IF EXISTS tbl_book; DROP TABLE IF EXISTS tbl_author")
    db.commit()

def create_authors_table(db):
    db.execute("CREATE TABLE tbl_author(id SERIAL PRIMARY KEY, name TEXT NOT NULL)")
    db.commit()

def create_books_table(db):
    db.execute("CREATE TABLE tbl_book(isbn TEXT PRIMARY KEY,"\
                                      "title TEXT NOT NULL,"\
                                      "author_id INTEGER NOT NULL REFERENCES tbl_author(id),"\
                                      "year TEXT NOT NULL"\
                                      ")")
    db.commit()


def insert_books(db):
    with open("books.csv","r") as file:
        reader = csv.reader(file)
        list_book = []
        list_author = []
        dict_author = {}
        id = 0

        for isbn, title, author, year in reader:
            if dict_author.get(author) is None:
                id = id + 1
                dict_author[author] = id;
                list_author.append({"id": id, "name": author})
            list_book.append({"isbn": isbn, "title": title, "author_id": dict_author[author], "year": year})

        db.execute("INSERT INTO tbl_author VALUES(:id, :name)", list_author)
        db.execute("INSERT INTO tbl_book VALUES(:isbn, :title, :author_id, :year)", list_book)
        db.commit()

def print_books_from_db(db):
    res = db.execute("SELECT (isbn, title, name, year) FROM tbl_book INNER JOIN tbl_author ON tbl_book.author_id = tbl_author.id")

    for x in res:
        print(x)


if __name__ == '__main__':
    main()
