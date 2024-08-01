import spotipy
from spotipy.oauth2 import SpotifyOAuth
from datetime import datetime
import json

def save_jason(file,data):
    with open(file, 'w', encoding='utf-8') as jf: 
        json.dump(data, jf, ensure_ascii=False, indent=4)


def extract_data(cli_id,secret,re_uri):

    #Client authorization:

    sp_oauth = SpotifyOAuth(
    client_id=cli_id,
    client_secret=secret,
    redirect_uri=re_uri,
    scope='user-read-recently-played, user-top-read')

    #Acces to user's spotify account:

    auth_url = sp_oauth.get_authorize_url()
    print(f'Please enter the following url to authenticate your spotify account: {auth_url}')
    print()

    try:
        response = input('Paste the url you were directed to after authenticating: ').strip()
        if not response:
            raise ValueError('Response was wrong, try it again')

        code = sp_oauth.parse_response_code(response)
        if not code:
            raise ValueError('The code could not be authenticated')

        token_info = sp_oauth.get_access_token(code, check_cache=False)
        if not token_info or 'access_token' not in token_info:
            raise ValueError('Could not obtain access token')

        spotify_status = spotipy.Spotify(auth=token_info['access_token'])

    except ValueError as e:
        print(f'Error: {e}')

    if spotify_status:
        print('Successful authentication')
        print()
        print('Getting tracks and artists info...')
        sp = spotify_status
    else:
        print('Authentication could not be completed. Try again...')
    
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