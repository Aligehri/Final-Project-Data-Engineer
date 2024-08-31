import pandas as pd
from modules import read_json
from sqlalchemy import create_engine
from decouple import config
import json

def load_data():
    user = config('user_rs')
    password = config('pass_rs')
    host = config('host_rs')
    port = config('port_rs')
    db = config('database_rs')
    schema = config('schema')

    conn = create_engine(f'postgresql://{user}:{password}@{host}:{port}/{db}')

    tracks_df = pd.DataFrame(read_json('tracks_transformed.json'))

    tracks_df.to_sql(
        f'tracks.{schema}',
        conn, 
        index=False,
        if_exists='replace')
  
    print()
    print()
    print("The process has finished")
    print('Check the database to see the data loaded')
