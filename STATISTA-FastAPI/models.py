from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from database import Base


class Project(Base):
    __tablename__ = "projects"

    ranking_id = Column(String, primary_key=True, index=True)
    ranking_name = Column(String)
    base_path = Column(String)
    ranking_logo_path = Column(String)

    ranking_positions = relationship("Ranking_Position", back_populates="project")

    def __str__(self):
        return f"{self.ranking_id}, {self.ranking_name}, {self.base_path}, {self.ranking_logo_path}"


class Ranking_Position(Base):
    __tablename__ = "ranking_positions"

    position_id = Column(String, primary_key=True, index=True)
    ranking_id = Column(String, ForeignKey("projects.ranking_id"))
    position_country = Column(Integer)
    position_world = Column(Integer)
    published_name = Column(String)
    city = Column(String)
    state = Column(String)
    country = Column(String)
    years_awarded = Column(String)
    sales_contact_id = Column(Integer, ForeignKey("sales_contacts.id"))

    project = relationship("Project", back_populates="ranking_positions")
    sales_contacts = relationship("Sales_Contact", back_populates="ranking_positions")

    def __str__(self):
        return f"{self.position_id}, {self.ranking_id}, {self.position_country}, {self.position_world}, {self.published_name}, {self.city}, {self.state}, {self.country}, {self.years_awarded}, {self.sales_contact_id}"


class Sales_Contact(Base):
    __tablename__ = "sales_contacts"

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String)
    last_name = Column(String)
    job_title = Column(String)
    phone = Column(String)
    email = Column(String)

    ranking_positions = relationship(
        "Ranking_Position", back_populates="sales_contacts"
    )

    def __str__(self):
        return f"{self.id}, {self.first_name}, {self.last_name}, {self.job_title}, {self.phone}, {self.email}"
