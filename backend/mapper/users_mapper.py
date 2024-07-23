#
# Lab FastAPI
#
# Date    : 2024-06-29
# Auther  : Hirotoshi FUJIBE
# History :
#

# Import Libraries
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql.functions import current_timestamp
from sqlalchemy.ext.declarative import declarative_base

# Base
user_list_base = declarative_base()


# USER_LIST
class UserList(user_list_base):
    __tablename__ = 'user_list'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(32), nullable=False, unique=True)
    password = Column(String(416), nullable=False)
    mail = Column(String(64), nullable=False, unique=True)
    remark = Column(String(768), nullable=False)
    created_at = Column(DateTime, server_default=current_timestamp())
    updated_at = Column(DateTime, server_default=current_timestamp())
