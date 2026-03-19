import re
import psycopg
import os
from dotenv import load_dotenv
load_dotenv()

DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_URI = f"postgresql://postgres:{DB_PASSWORD}@localhost:5432/postgres"

with open("baby2008.html") as file:
    html = file.read()
    raw_names = re.findall(r'<td>([^0-9]+?)</td>', html)
    data = [(name,) for name in raw_names]

with psycopg.connect(DB_URI) as conn:
    with conn.cursor() as cur:
        create_table = """
        CREATE TABLE IF NOT EXISTS baby_names(
            id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
            baby_name TEXT NOT NULL
        )
        """
        cur.execute(create_table)
        print("Table created successfully")

        insert_names = """
        INSERT INTO baby_names(baby_name) VALUES (%s)
         """
        cur.executemany(insert_names, data)
        conn.commit()

