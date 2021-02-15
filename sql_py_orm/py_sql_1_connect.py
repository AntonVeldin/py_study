import sqlalchemy
import psycopg2
import json
from sqlalchemy.orm import sessionmaker

with open("token.json", 'r') as f:
    js = json.loads(f.read())
db_name = js["database"]["name"]
db_user = js["database"]["user"]
db_pass = js["database"]["pass"]

db = 'postgresql://' + db_user + ':' + db_pass + '@localhost:5432/' + db_name


connect = psycopg2.connect(db)
with connect.cursor() as cursor:
    cursor.execute('SELECT * FROM tracks')

print('-----1')

engine = sqlalchemy.create_engine(db)
with engine.connect() as connection:
    result = connection.execute('SELECT * FROM albums')

# ??

print('-----2')

engine = sqlalchemy.create_engine(db)
# connection = engine.connect()
print(engine.table_names())

print('-----3')




