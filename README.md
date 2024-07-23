# lab-fast_api

## License

MIT

## How to run the WebAPI backend web server

On command prompt.

```bat:Command Prompt
> d:
> cd d:\path\of\project\backend
> pip install uvicorn fastapi
> pip install sqlalchemy sqlalchemy_utils mysql-connector-python pycryptodome
> pip install python-jose[cryptography] passlib[bcrypt]
> python.exe .\database\create_database.py
> python.exe backend_main.py
```

## How to run the React frontend web server

On command prompt.

```bat:Command Prompt
> d:
> cd d:\path\of\project
> npx create-react-app frontend --template typescript
> cd frontend
> npm install react-router-dom
> npm install @mui/material @emotion/react @emotion/styled
> npm run build
> python.exe frontend_main.py
```

## How to access the web page

Access url 'http://localhost:3000' on browser
