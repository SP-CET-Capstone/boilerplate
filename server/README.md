## 1. Create .env file

Create .env file in the server folder with the following content:

```
DB_HOST=localhost
DB_DATABASE=movies
DB_USER=root
DB_PASSWORD=password
```

Replace the above values accordingly

The `.env` file is meant to contain secrets, thus it is not checked into git, thus it is unique to you.

## 2. Install dependencies

```
pip install -r requirements.txt
```

## 3. Start server

```
python ./app.py
```
