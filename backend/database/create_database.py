#
# Lab FastAPI
#
# Date    : 2024-06-29
# Author  : Hirotoshi FUJIBE
# History :
#

# Import Libraries
import sys
from sqlalchemy import create_engine, text
from sqlalchemy_utils import create_database, drop_database
from sqlalchemy.orm import sessionmaker, scoped_session
from backend.mapper.products_mapper import product_list_base
from backend.mapper.users_mapper import user_list_base

# Display
print('lab-FastAPI - DDL/DML')
print('root password is "********"')
password = input('Enter password: ')

# Constants
DIALECT = 'mysql'
DRIVER = 'mysqlconnector'
USER = 'root'
HOST = 'localhost'
PORT = '3306'
DB = 'lab_fast'
DATABASE = f'{DIALECT}+{DRIVER}://{USER}:{password}@{HOST}:{PORT}/{DB}?charset=utf-8'

CMD_DDLS = [
    text('DROP ROLE IF EXISTS lab_fast_role'),
    text('CREATE ROLE lab_fast_role'),
    text('DROP USER IF EXISTS \'lab_fast_user\'@\'localhost\''),
    text('CREATE USER \'lab_fast_user\'@\'localhost\' IDENTIFIED BY \'Asdf1234\' DEFAULT ROLE lab_fast_role'),
    text('GRANT SELECT, INSERT, UPDATE, DELETE ON lab_fast.product_list TO lab_fast_role'),
    text('GRANT SELECT, INSERT, UPDATE, DELETE ON lab_fast.user_list TO lab_fast_role'),
]
CMD_DMLS = [
    text('''
        INSERT INTO LAB_FAST.PRODUCT_LIST ( NAME, REMARK ) VALUES
            ( 'Apple', 'Made in Japan.' ),
            ( 'Orange', 'Made in America.' )
    '''),
    text('''
        INSERT INTO LAB_FAST.USER_LIST ( NAME, PASSWORD, MAIL, REMARK ) VALUES
            ( 'root', HEX(AES_ENCRYPT('Asdf1234', 'Asdf1234Asdf1234')), 'root@xxxx.com', 'Administrator' ),
            ( 'power-user', HEX(AES_ENCRYPT('Asdf1234', 'Asdf1234Asdf1234')), 'power.user@xxxx.com', 'Power User' )
    '''),
]


# Main
def main() -> None:

    # Engine
    engine = create_engine(DATABASE, echo=True)
    session = scoped_session(sessionmaker(autocommit=True, autoflush=True, bind=engine))

    # Drop Database
    try:
        drop_database(engine.url)
    except Exception:    # noqa
        pass

    # Create Database
    create_database(engine.url)
    conn = engine.connect()
    product_list_base.metadata.create_all(bind=engine)
    product_list_base.query = session.query_property()
    user_list_base.metadata.create_all(bind=engine)
    user_list_base.query = session.query_property()

    # Grant
    for cmd in CMD_DDLS:
        _ = conn.execute(cmd)
        conn.commit()

    # Insert Test Data
    for cmd in CMD_DMLS:
        _ = conn.execute(cmd)
        conn.commit()

    sys.exit(0)


# Goto Main
if __name__ == '__main__':
    main()
