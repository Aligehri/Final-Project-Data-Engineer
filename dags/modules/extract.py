import spotipy
from spotipy.oauth2 import SpotifyOAuth
from datetime import datetime
from decouple import config
import json

def save_jason(file,data):
    with open(file, 'w', encoding='utf-8') as jf: 
        json.dump(data, jf, ensure_ascii=False, indent=4)


def extract_data():

    #Client authorization:

    sp = spotipy.Spotify( auth_manager = SpotifyOAuth(
    client_id=config('SPOTIPY_CLIENT_ID'),
    client_secret=config('SPOTIPY_CLIENT_SECRET'),
    redirect_uri=config('SPOTIPY_REDIRECT_URI'),
    scope='user-read-recently-played, user-top-read'))
    
    #Set time from the begining of the year:

    current_time = datetime.now()
    date = current_time.replace(month= 1, day = 1, hour=0, minute=0, second=0, microsecond=0)
    date_timestamp = int(date.timestamp())

    #Get recently played tracks, top tracks and top artist from long term:

    recently = sp.current_user_recently_played(limit=50, after=date_timestamp)
    top_tracks = sp.current_user_top_tracks(limit=50,offset=0,time_range='long_term')
    top_artists = sp.current_user_top_artists(limit=50,offset=0,time_range='long_term')

    save_jason('recently.json',recently)
    save_jason('top_tracks.json',top_tracks)
    save_jason('top_artists.json',top_artists)
