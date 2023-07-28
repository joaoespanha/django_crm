import mysql.connector
import os
from dotenv import load_dotenv
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent

# Load environment variables from .env file
load_dotenv(os.path.join(BASE_DIR, ".env"))

# Now you can access the environment variables using the `os.getenv()` function
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")


data_base = mysql.connector.connect(host="localhost", user=DB_USER, passwd=DB_PASSWORD)


cursor_object = data_base.cursor()


cursor_object.execute("CREATE DATABASE crm_database")

print(DB_PASSWORD)
