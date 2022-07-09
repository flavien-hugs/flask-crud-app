# Flask CRUD (CREATE - READ - UPDATE - DELETE) APP

[![Django Version](https://img.shields.io/badge/Django-Version3-success.svg)](https://www.djangoproject.com)
[![Python Version](https://img.shields.io/badge/Python-3.6-brightgreen.svg)](https://www.python.com)

![Flask CRUD](https://github.com/flavien-hugs/flask-crud-app/blob/main/screenshort.png)

[flask-crud-app](https://github.com/flavien-hugs/flask-crud-app/) is a simple application flask to implement CRUD.

#### Installation & Execution of the project locally

* Clone project
```
git clone https://github.com/flavien-hugs/flask-crud-app.git
cd flask-crud-app
```

* Initialzed database
```
make db
or
FLASK_APP=run.py flask init_db
```

* Activate the virtual environment and install the dependencies with the command
```
make install
or 
pipenv install
pipenv shell
```

Finally, start the internal flask server with
```
python run.py
```

Navigate to
```
<http://localhost:5000>
```

Good code :)
