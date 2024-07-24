#
# Lab FastAPI - frontend
#
# Date    : 2024-07-23
# Author  : Hirotoshi FUJIBE
# History :
#


# Import Libraries

# import os
# import sys
import uvicorn

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.exceptions import HTTPException
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

# FastAPI Settings
app = FastAPI(docs_url=None, redoc_url=None, openapi_url=None)
app.mount(path='/static', app=StaticFiles(directory='.\\build\\static'), name='static')
templates = Jinja2Templates(directory='.\\build')


# / (Return index.html)
@app.get("/", response_class=HTMLResponse)
async def root(request: Request):
    return templates.TemplateResponse('index.html', {'request': request})


# When Manipulate [Rewind] [Forward] [Refresh] Button [URL] Textbox at Browser
@app.exception_handler(404)
async def not_found(request: Request, ex: HTTPException):    # noqa
    return templates.TemplateResponse('index.html', {'request': request})


# React Frontend Web Server
if __name__ == '__main__':
#    sys.stdout = open(os.devnull, 'w')    # Discard stdout
#    sys.stderr = open(os.devnull, 'w')    # Discard stderr
    uvicorn.run(app, host='0.0.0.0', port=3000)
