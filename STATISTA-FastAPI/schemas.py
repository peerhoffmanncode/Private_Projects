from sqlalchemy.orm import relationship
from pydantic import BaseModel, Field, validator
from typing import Optional, Union
import json


class RankingName(BaseModel):
    de: Optional[str]
    en: Optional[str]
    es: Optional[str]
    fr: Optional[str]
    it: Optional[str]


class SalesContactsBase(BaseModel):
    # id: Optional[int]
    first_name: Optional[str] = Field(..., alias="sales_contact_first_name")
    last_name: Optional[str] = Field(..., alias="sales_contact_last_name")
    job_title: Optional[str] = Field(..., alias="sales_contact_job_title")
    phone: Optional[str] = Field(..., alias="sales_contact_phone")
    email: Optional[str] = Field(..., alias="sales_contact_email")

    class Config:
        orm_mode = True
        allow_population_by_field_name = True


class RankingPositionsBase(BaseModel):
    # position_id: Optional[str]
    # ranking_id: Optional[str]
    position_country: Optional[int | None]
    position_world: Optional[int | None]
    published_name: Optional[str]
    city: Optional[str]
    state: Optional[str]
    country: Optional[str]
    years_awarded: Optional[list[int]]

    @validator("years_awarded", pre=True)
    def string_to_List2(cls, value):
        if not isinstance(value, list):
            return value.split(",")
        return value

    @validator("position_country", "position_world", pre=True)
    def string_to_none(cls, value):
        if isinstance(value, str):
            return None
        return value

    class Config:
        orm_mode = True
        allow_population_by_field_name = True


class RankingPositions(RankingPositionsBase):

    sales_contacts: Optional[list[SalesContactsBase]]

    @validator("sales_contacts", pre=True)
    def string_to_List1(cls, value):
        if not isinstance(value, list):
            return [value]
        return value

    class Config:
        orm_mode = True
        allow_population_by_field_name = True


class ProjectsBase(BaseModel):
    ranking_id: Optional[str]
    ranking_name: Optional[dict]
    ranking_project_path: Optional[RankingName]
    ranking_logo_path: Optional[str]

    @validator("ranking_name", "ranking_project_path", pre=True)
    def string_to_dict(cls, value):
        if not isinstance(value, dict):
            return json.loads(value)
        return value

    class Config:
        orm_mode = True
        allow_population_by_field_name = True


class ProjectsRankingsSales(ProjectsBase):

    ranking_positions: list[RankingPositions] = []

    class Config:
        orm_mode = True
        allow_population_by_field_name = True
