#!/usr/bin/python3
"""Module for DBStorage class"""
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import Base
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class DBStorage:
    """Grace created DBStorage class"""
    __engine = None
    __session = None

    def __init__(self):
        """Grace Initialize DBStorage instance"""
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                                      .format(os.getenv('HBNB_MYSQL_USER'),
                                              os.getenv('HBNB_MYSQL_PWD'),
                                              os.getenv('HBNB_MYSQL_HOST',
                                                        'localhost'),
                                              os.getenv('HBNB_MYSQL_DB')),
                                      pool_pre_ping=True)
        if os.getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Grace Query on the current database session"""
        from models import storage
        classes = [User, State, City, Amenity, Place, Review]
        if cls:
            classes = [cls]
        objects = {}
        for cls in classes:
            for obj in self.__session.query(cls):
                key = '{}.{}'.format(type(obj).__name__, obj.id)
                objects[key] = obj
        return objects

    def new(self, obj):
        """Grace Add the object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """Grace commit all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """Grace Delete from the current database session"""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """Grace create all tables in hte database and
            create current session"""
        from models import storage
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()
