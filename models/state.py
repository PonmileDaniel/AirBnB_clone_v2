#!/usr/bin/python3
""" State Module for HBNB project """
import os
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


STORAGE_TYPE = os.getenv('HBNB_TYPE_STORAGE', 'fs')

class State(BaseModel):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    name = ""

    """Grace updates the state models with given attribute"""
    if STORAGE_TYPE == 'db':
        cities = relationship("City", cascade="all, delete-orphan",
                              backref="state")
    else:
        @property
        def cities(self):
            """Grace updates Getter attribute that returns the list of City
                instances with state_id equals to the cuurent State."""
            from models import storage
            city_list = []
            for city in storage.all(City).values():
                if city.state_id == self.id:
                    city_list.append(city)
            return city_list
