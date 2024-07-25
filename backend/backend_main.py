#
# Lab FastAPI - backend
#
# Date    : 2024-06-27
# Author  : Hirotoshi FUJIBE
# History :
#

# When wrote this source code, referred this page 'https://fastapi.tiangolo.com/ja/tutorial/security/oauth2-jwt/'

# Import Libraries

# import os
# import sys
import uvicorn

import secrets
from jose import JWTError, jwt
from typing import Optional
from pydantic import BaseModel
from datetime import datetime, timedelta

from fastapi import FastAPI, Depends, HTTPException, Request, Response, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware

from action.authenticate_user_action import get_user_and_password, get_user
from action.manipulate_products_action import read_products
from backend.response.status_response import JsonStatusResponse

# Constants
SECRET_KEY = secrets.token_hex(32)  # example: 'c13b4b4808d0eed9323e44897315b4fea0c023313585afd9c0d6896e769490fe'
ALGORITHM = 'HS256'
ACCESS_TOKEN_EXPIRE_MINUTES = 30
ORIGINS = [
    'http://localhost:3000',
]


# Token
class Token(BaseModel):
    access_token: str
    token_type: str


# TokenData
class TokenData(BaseModel):
    username: Optional[str] = None


# User
class User(BaseModel):
    username: str


# FastAPI Settings
app = FastAPI(docs_url=None, redoc_url=None, openapi_url=None)
app.mount(path='/static', app=StaticFiles(directory='.\\templates\\static'), name='static')
app.add_middleware(
    CORSMiddleware,    # noqa
    allow_origins=ORIGINS,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)
templates = Jinja2Templates(directory='.\\templates')

# OAuth2
oauth2_scheme = OAuth2PasswordBearer(tokenUrl='token')


# Create JWT at /token Endpoint Request
def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({'exp': expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


# Check JWT Is Valid or Not at Some Endpoint Request
async def get_current_user(request: Request):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail='Could not validate credentials',
        headers={'WWW-Authenticate': 'Bearer'},
    )
    token = ''
    # read from request header of 'Cookie: access_token={access_token}'
    cookie = request.cookies.get('access_token')
    if cookie is not None and cookie != '':
        token = cookie
    # read from request header of 'Authorization: "Bearer {access_token}"'
    authorization = request.headers.get('Authorization')
    if authorization is not None and authorization != '':
        scheme, _, token = authorization.partition(' ')
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get('username')
        if username is None:
            raise credentials_exception
        token_data = TokenData(username=username)
    except JWTError:
        raise credentials_exception
    user = get_user(username=token_data.username)
    if user is None:
        raise credentials_exception
    return user


# / (Return index.html)
@app.get("/", response_class=HTMLResponse)
async def root(request: Request):
    return templates.TemplateResponse('index.html', {'request': request, 'message': 'hello world'})


# /auth (Return the JWT on Response Header/Body)
@app.post('/auth', response_model=Token)
async def login_for_access_token(
        response: Response, form_data: OAuth2PasswordRequestForm = Depends()):
    user = get_user_and_password(form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='Incorrect username or password',
            headers={'WWW-Authenticate': 'Bearer'}
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={'username': user.username}, expires_delta=access_token_expires
    )
    # write to response header of 'Set-Cookie: access_token={access_token}'
    response.set_cookie(key='access_token', value=f'{access_token}', httponly=True, secure=True, samesite='none')
    # return to value of JSON
    return {'access_token': access_token, 'token_type': 'bearer'}


# /unauth (No Error Process)
@app.post('/unauth')
async def unauth(response: Response):
    # write to response header of 'Set-Cookie: access_token=""'
    response.delete_cookie(key="access_token", httponly=True, secure=True, samesite='none')
    return JsonStatusResponse()


# /is_valid (Need the JWT on Request Header)
@app.post('/is_valid')
async def is_valid(current_user: User = Depends(get_current_user)):    # noqa
    return JsonStatusResponse()


# /products (Need the JWT on Request Header)
@app.get('/products')
async def get_products(current_user: User = Depends(get_current_user)):    # noqa
    return read_products()


# Web API Backend Web Server
if __name__ == '__main__':
#    sys.stdout = open(os.devnull, 'w')    # Discard stdout
#    sys.stderr = open(os.devnull, 'w')    # Discard stderr
    uvicorn.run(app, host='0.0.0.0', port=3001, server_header=False)
