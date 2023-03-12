import csv
import ast
from sqlalchemy.orm import Session

from database import SessionLocal

db = SessionLocal()


class Importer:
    """
    class to import a csv file
    """

    @staticmethod
    def read_csv(filename: str, DB_Model):
        """
        open a csv file and read data from file and write to the database
        """
        try:
            with open(filename, "r") as csv_file:
                # loda csv file content
                content = csv.DictReader(csv_file)

                for row in content:
                    # get the first colum of the csv - probably the ID
                    key, value = next(iter(row.items()))

                    # if the ID doesn't exist, create it!
                    if (
                        not db.query(DB_Model)
                        .filter(getattr(DB_Model, key) == value)
                        .first()
                    ):
                        db.add(DB_Model(**row))
                        db.commit()

        except FileNotFoundError:
            raise FileNotFoundError("could not correctly load file!")

    @staticmethod
    def write_csv(filename: str, DB_Model):
        """
        to be implemented
        """
        raise NotImplementedError
