#!/usr/bin/python3
"""New engine DBStorage"""
from os import getenv
from sqlalchemy import create_engine


class DBStorage:
    """this is the class DBStorage"""
    __engine = None
    __session = None

    def __init__(self):
        """constructor"""
        from models.base_model import Base
        user = getenv("HBNB_MYSQL_USER")
        pwd = getenv("HBNB_MYSQL_PWD")
        host = getenv("HBNB_MYSQL_HOST")
        db = getenv("HBNB_MYSQL_DB")
        link = "mysql+mysqldb://{}:{}@{}/{}".format(user, pwd, host, db)
        self.__engine = create_engine(link, pool_pre_ping=True)
        if getenv("HBNB_ENV") == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """query all objects"""
        from models.user import User
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review
        dict = {}
        classes = [User, State, City, Amenity, Place, Review]
        if cls is None:
            for i in classes:
                res = self.__session.query(i).all()
                for v in res.values():
                    k = "{}.{}".format(i, v.id)
                    setattr(dict, k, v)
        else:
            res = self.__session.query(cls).all()
            for v in res.values():
                k = "{}.{}".format(cls, v.id)
                setattr(dict, k, v)
        return dict
