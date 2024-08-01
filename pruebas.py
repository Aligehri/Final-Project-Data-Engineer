import spotipy
from spotipy.oauth2 import SpotifyOAuth
from datetime import datetime
from decouple import config
import pandas as pd

SPOTIPY_CLIENT_ID=config('SPOTIPY_CLIENT_ID')
SPOTIPY_CLIENT_SECRET=config('SPOTIPY_CLIENT_SECRET')
SPOTIPY_REDIRECT_URI = config('SPOTIPY_REDIRECT_URI')

sp_oauth = SpotifyOAuth(
    client_id=SPOTIPY_CLIENT_ID,
    client_secret=SPOTIPY_CLIENT_SECRET,
    redirect_uri=SPOTIPY_REDIRECT_URI,
    scope='user-read-recently-played, user-top-read')

auth_url = sp_oauth.get_authorize_url()
print(f'Por favor, navega a la siguiente URL para autenticar: {auth_url}')
response = input('Pega la URL que te redirigió Spotify después de autenticarse: ')
code = sp_oauth.parse_response_code(response)
token_info = sp_oauth.get_access_token(code, check_cache=False)

sp = spotipy.Spotify(auth=token_info['access_token'])

current_time = datetime.now()
date = current_time.replace(month= 1, day = 1, hour=0, minute=0, second=0, microsecond=0)
date_timestamp = int(date.timestamp())

recently = sp.current_user_recently_played(limit=2, after=date_timestamp)
top_tracks = sp.current_user_top_tracks(limit=50,offset=0,time_range='long_term')
top_artists = sp.current_user_top_artists(limit=2,offset=0,time_range='long_term')


"""for item in recently['items']:
    track = item['track']
    artist = item['track']['artists'][0]['name']
    duration = round(item['track']['duration_ms']/60000,2)
    day_played = item['track]['played_at'][0:10]
    time_played = item['track']['played_at'][11:22]
    played_from = item['track']['context']['type']

    print(f"{track['name']} by {track['artists'][0]['name']}")"""



print()
print()
print()

top_tracks_df = {'Track name':[], 'Artist':[], 'Album':[], 'Genres':[], 'Duration min':[], 'Release date':[], 'Popularity':[], 'Track id':[] }

for item in top_tracks['items']:
    top_tracks_df['Track name'].append(item['name'])
    top_tracks_df['Artist'].append(item['artists'][0]['name'])
    top_tracks_df['Album'].append(item['album']['name'])
    top_tracks_df['Genres'].append(sp.artist(item['artists'][0]['id'])['genres'])
    top_tracks_df['Duration min'].append(round(item['duration_ms']/60000, 2))
    top_tracks_df['Release date'].append(item['album']['release_date'])
    top_tracks_df['Popularity'].append(item['popularity'])
    top_tracks_df['Track id'].append(item['id'])

top_tracks_df = pd.DataFrame(top_tracks_df)

print(top_tracks_df)

print(results)