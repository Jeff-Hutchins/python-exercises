import pandas as pd
from env import host, user, password

database_name = "albums_db"

url = f'mysql+pymysql://{user}:{password}@{host}/{database_name}'

# df = pd.read_sql('SELECT * FROM employees LIMIT 5 OFFSET 50', url)
# print(df)

query = """SELECT * FROM albums"""

df = pd.read_sql(query, url)
print(df)