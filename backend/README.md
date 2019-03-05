# Backend

## Virtual Env

To support vscode better, these command should be run at root level of this project

```bash
## At SENG3011_Neon/
virtualenv venv  -p `where python3`
pip install -r backend/requirements.txt
## setup the database
./manage.py migrate
```

Then you can run the server

```bash
./manage.py runserver
```
