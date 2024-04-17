#Before running script I set up a Docker Container: 
#docker run --name recycle-me-db -e POSTGRES_DB=recycle_me -e POSTGRES_USER=wyliebrown1990 -e POSTGRES_PASSWORD=test123 -p 5432:5432 -d postgres
#Docker ID: 55962f6a5a96
#Container Name: recycle-me-db
#Execute this code in terminal: '''python setup_database.py'''

#Step 1: Install psycopg2 library, which is a PostgreSQL database adapter for Python
#pip install psycopg2-binary

#Step 2: Create Python Script for Database Setup
import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

# Connection parameters
db_name = "recycle_me"
user = "wyliebrown1990"
password = "test123"
host = "localhost"

# Connect to PostgreSQL server
conn = psycopg2.connect(dbname="postgres", user=user, password=password, host=host)
conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)

# Cursor to perform database operations
cur = conn.cursor()

# Create database
try:
    cur.execute(f"CREATE DATABASE {db_name}")
    print(f"Database {db_name} created successfully.")
except psycopg2.Error as e:
    print(f"Error: {e}")
    print(f"Database {db_name} may already exist.")

# Connect to the newly created database
conn.close()
conn = psycopg2.connect(dbname=db_name, user=user, password=password, host=host)
cur = conn.cursor()

# SQL commands to create tables
commands = (
    """
    CREATE TABLE locations (
        location_id SERIAL PRIMARY KEY,
        name VARCHAR(255) UNIQUE NOT NULL
    )
    """,
    """
    CREATE TABLE materials (
        material_id SERIAL PRIMARY KEY,
        name VARCHAR(255) UNIQUE NOT NULL
    )
    """,
    """
    CREATE TABLE items (
        item_id SERIAL PRIMARY KEY,
        name VARCHAR(255) NOT NULL,
        material_id INTEGER REFERENCES materials(material_id),
        location_id INTEGER REFERENCES locations(location_id)
    )
    """,
    """
    CREATE TABLE unavailable_locations (
        entry_id SERIAL PRIMARY KEY,
        location_name VARCHAR(255) NOT NULL,
        input_timestamp TIMESTAMP NOT NULL DEFAULT NOW()
    )
    """,
    """
    CREATE TABLE non_recyclable_items (
        entry_id SERIAL PRIMARY KEY,
        item_name VARCHAR(255) NOT NULL,
        input_timestamp TIMESTAMP NOT NULL DEFAULT NOW()
    )
    """
)

# Execute commands to create tables
for command in commands:
    cur.execute(command)

print("Tables created successfully.")

# Close communication with the database
cur.close()
conn.close()
