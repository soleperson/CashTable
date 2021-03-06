from sqlalchemy import Column, String, create_engine, Integer, Float, func, distinct
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from reference import  AssetsCategory

_base = declarative_base()
DATABASE_NAME = 'cash_table'
HOST = 'localhost'
USERNAME = 'root'
PASSWORD = '123456789...'
PORT = 3306
_engine = create_engine(f"mysql://{USERNAME}:{PASSWORD}@{HOST}:{PORT}/{DATABASE_NAME}")

class Assets(_base):
    __tablename__ = 'assets'
    id = Column(Integer, primary_key=True, autoincrement=True)
    project = Column(String(20), default='')
    category = Column(Integer, default=AssetsCategory.STATIC)
    balance = Column(Float, default=0.0)


class Debt(_base):
    __tablename__ = 'debt'
    id = Column(Integer, primary_key=True, autoincrement=True)
    project = Column(String(20), default='')
    balance = Column(Float, default=0.0)


class Income(_base):
    __tablename__ = 'income'
    id = Column(Integer, primary_key=True, autoincrement=True)
    project = Column(String(20), default='')
    balance = Column(Float, default=0.0)


class Expenses(_base):
    __tablename__ = 'expenses'
    id = Column(Integer, primary_key=True, autoincrement=True)
    project = Column(String(20), default='')
    balance = Column(Float, default='')


_base.metadata.bind = _engine
_base.metadata.create_all()
_session = sessionmaker(bind=_engine)

session = _session()


def sum_models(model):
    result = session.query(func.sum(model.balance)).scalar()
    if not result:
        return 0
    return round(result, 2)
