import pandas as pd
from modules import read_json
from sqlalchemy import create_engine
from decouple import config
import json

def load_data(user, password, host, port, db, schema):

    conn = create_engine(f'postgresql://{user}:{password}@{host}:{port}/{db}')

    recently_df = pd.DataFrame(read_json('recently_transformed.json'))
    top_tracks_df = pd.DataFrame(read_json('top_tracks_transformed.json'))
    top_artists_df = pd.DataFrame(read_json('top_artists_transformed.json'))

    recently_df.to_sql(
        f'recently_played.{schema}',
        conn, 
        index=False,
        if_exists='replace')

    top_tracks_df.to_sql(
        f'top_tracks.{schema}',
        conn, 
        index=False,
        if_exists='replace')

    top_artists_df.to_sql(
        f'top_artists.{schema}',
        conn, 
        index=False,
        if_exists='replace')
    
    print()
    print()
    print("The process has finished")
    print('Check the database to see the data loaded')
