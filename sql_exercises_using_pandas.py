# use database albums_db and albums table

def get_db_url(database_name, sub_query):
    import pandas as pd
    import numpy as np
    from env import host, user, password
    url = f'mysql+pymysql://{user}:{password}@{host}/{database_name}'
    query = f"SELECT * FROM {database_name}"
    database_name = pd.read_sql(sub_query, url)
    return database_name

get_db_url("albums_db", "albums")

# Basic Statements

# Write queries to find the following information.

# The name of all albums by Pink Floyd

albums = get_db_url("albums_db", "albums")
albums

albums[albums['artist'] == 'Pink Floyd']
#   or
albums['name'][albums['artist'] == 'Pink Floyd']

# The year Sgt. Pepper's Lonely Hearts Club Band was released

albums[albums['name'].str.contains("Sgt")]
#   or
albums['release_date'][albums['name'].str.contains("Sgt")]

# The genre for the album Nevermind

albums[albums['name'] == 'Nevermind']

# Which albums were released in the 1990s

albums[albums['release_date'].between(1990, 2000)]

# Which albums had less than 20 million certified sales

albums[albums['sales'] < 28.0]

# of "Hard rock" or "Progressive rock"?

albums[albums['genre'].str.contains('Hard rock' or 'Progressive rock')]

