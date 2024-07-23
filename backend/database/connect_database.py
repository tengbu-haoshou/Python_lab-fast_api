#
# Lab FastAPI
#
# Date    : 2024-06-29
# Auther  : Hirotoshi FUJIBE
# History :
#

# Import Libraries
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session

# Constants
DIALECT = 'mysql'
DRIVER = 'mysqlconnector'
USER = 'lab_fast_user'
PASSWORD = 'Asdf1234'
HOST = 'localhost'
PORT = '3306'
DATABASE = 'lab_fast'
DATABASE = f'{DIALECT}+{DRIVER}://{USER}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}?charset=utf-8'

# Engine
engine = create_engine(DATABASE, echo=True)    # True: SQL statement log
session_local = sessionmaker(autocommit=False, autoflush=False, bind=engine)
session = scoped_session(session_local)
