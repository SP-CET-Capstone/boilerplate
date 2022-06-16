import os
from dotenv import load_dotenv

load_dotenv()

# Create pool with these variables
# Remember to specify their values in .env first (See README on creating .env)
host = os.getenv('DB_HOST')
database = os.getenv('DB_DATABASE')
user = os.getenv('DB_USER')
password = os.getenv('DB_PASSWORD')
