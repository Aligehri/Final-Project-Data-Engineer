import pandas as pd
from modules import read_json
from sqlalchemy import create_engine
from decouple import config
import json

def load_data(user, password, host, port, db ):

    conn = create_engine(f'postgresql://{user}:{password}@{host}:{port}/{db}')

    recently_df = pd.DataFrame(read_json('recently_transformed.json'))
    top_tracks_df = pd.DataFrame(read_json('top_tracks_transformed.json'))
    top_artists_df = pd.DataFrame(read_json('top_artists_transformed.json'))

    recently_df.to_sql(
        'recently_played.ghazzael5h_coderhouse',
        conn, 
        index=False,
        if_exists='replace')

    top_tracks_df.to_sql(
        'top_tracks.ghazzael5h_coderhouse',
        conn, 
        index=False,
        if_exists='replace')

    top_artists_df.to_sql(
        'top_artists.ghazzael5h_coderhouse',
        conn, 
        index=False,
        if_exists='replace')