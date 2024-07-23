#
# Lab FastAPI
#
# Date    : 2024-06-29
# Auther  : Hirotoshi FUJIBE
# History :
#

# Import Libraries
import binascii
from Crypto.Cipher import AES
from backend.mapper import users_mapper as model
from backend.database import connect_database as connect

# Crypto Key
CRYPTO_KEY = 'Asdf1234Asdf1234'


# Strip Padding String From ECB Decrypto String
def unpad(s):
    return s[:-ord(s[len(s) - 1:])]


# Decrypto
def decrypto(password_aes) -> str:
    password_bin = binascii.unhexlify(password_aes)
    decipher = AES.new(CRYPTO_KEY.encode('utf-8'), AES.MODE_ECB)
    dec = decipher.decrypt(password_bin)
    return unpad(dec).decode('utf-8')


# Get User and Verify Password
def get_user_and_password(username: str, password: str) -> []:
    user_list = connect.session.query(
        model.UserList.name.label("username"),
        model.UserList.password).filter(model.UserList.name == username).first()
    password_aes = user_list[1]    # column name "password"
    password_dec = decrypto(password_aes)
    if password != password_dec:
        return False
    return user_list


# Get User
def get_user(username: str) -> []:
    user_list = connect.session.query(
        model.UserList.name.label("username")).filter(model.UserList.name == username).first()
    return user_list
