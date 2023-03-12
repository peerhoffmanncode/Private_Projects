from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session, joinedload

import models, schemas
from typing import List

from database import SessionLocal, engine, Base
from importer import Importer

# initialize FastAPI app
app = FastAPI()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# build database tables
Base.metadata.create_all(bind=engine)

# read CSV files and build database records
Importer().read_csv(filename="data/projects.csv", DB_Model=models.Project)
Importer().read_csv(
    filename="data/ranking_positions.csv", DB_Model=models.Ranking_Position
)
Importer().read_csv(filename="data/sales_contacts.csv", DB_Model=models.Sales_Contact)


@app.get("/projects/", response_model=List[schemas.ProjectsBase])
def get_projects(db: Session = Depends(get_db)):
    return db.query(models.Project).all()


@app.get("/ranking_positions/", response_model=List[schemas.RankingPositionsBase])
def get_ranking_position(db: Session = Depends(get_db)):
    return db.query(models.Ranking_Position).all()


@app.get("/sales_contacts/", response_model=List[schemas.SalesContactsBase])
def get_sales_contacts(db: Session = Depends(get_db)):
    sales_contacts = db.query(models.Sales_Contact).all()
    return sales_contacts


@app.get("/all", response_model=List[schemas.ProjectsRankingsSales])
def get_it_all(db: Session = Depends(get_db)):
    projects = db.query(models.Project).all()
    return projects
