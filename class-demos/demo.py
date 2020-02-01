import psycopg2

conn = psycopg2.connect("dbname=example")

cursor = conn.cursor()

# Open a cursor to perform database operations
cur = conn.cursor()

# drop any existing todos table
cur.execute("DROP TABLE IF EXISTS table2;")

# (re)create the todos table
# (note: triple quotes allow multiline text in python)
cur.execute("""
  CREATE TABLE table2 (
    id INTEGER PRIMARY KEY,
    completed BOOLEAN NOT NULL DEFAULT False
  );
""")

cur.execute('INSERT INTO table2 (id, completed) VALUES (1, true);')

# commit, so it does the executions on the db and persists in the db
conn.commit()

cur.close()
conn.close()
