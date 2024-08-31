import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from decouple import config
import json

def save_jason(file,data):
    with open(file, 'w', encoding='utf-8') as jf: 
        json.dump(data, jf, ensure_ascii=False, indent=4)


def extract_data(exec_date, path):

    #Client authorization:

    auth_manager = SpotifyClientCredentials(
        client_id=config('SPOTIPY_CLIENT_ID'),
        client_secret=config('SPOTIPY_CLIENT_SECRET')
    )
    sp = spotipy.Spotify(auth_manager=auth_manager)

    #Get recently played tracks, top tracks and top artist from long term:

    playlist_id='37i9dQZF1DX37bXS7EGI3f'
    respuesta=sp.playlist(playlist_id, fields='tracks', market='MX', additional_types=('track',))

    save_jason('playlist_info.json',respuesta)
