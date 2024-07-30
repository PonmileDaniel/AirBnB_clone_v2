#!/usr/bin/python3
""" State Module for HBNB project """
import os
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


STORAGE_TYPE = os.getenv('HBNB_TYPE_STORAGE', 'fs')


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'

    if STORAGE_TYPE == 'db':
        name = Column(String(128), nullable=False)
        cities = relationship("City", cascade="all, delete-orphan",
                              backref="state")
    else:
        name = ""

        @property
        def cities(self):
            """Getter attribute that returns the list of City instances
               with state_id equals to the current State."""
            from models import storage
            from models.city import City
            city_list = []
            for city in storage.all(City).values():
                if city.state_id == self.id:
                    city_list.append(city)
            return (city_list)
