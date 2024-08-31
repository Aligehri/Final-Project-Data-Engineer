import json
import pandas as pd
import datetime
from modules import save_jason

def read_json(file):
    try:
        with open(file, 'r', encoding='utf-8') as file:
            return json.load(file)
    except FileNotFoundError:
        print(f'El archivo {file} no se encuentra.')
        return None

#Need to check key by key because there might not be a dictionary within another dictionary:

def check_data(item, keys):
    value = item
    for key in keys:
        if value is not None and key in value:
            value = value[key]
        else:
            return "No data"
    return value

def transform_data(exec_date, path):

    tracks = read_json('playlist_info.json')

    #Create dicts to append data:

    tracks_df={
        'Name':[],
        'Artist':[],
        'Album':[],
        'Genres':[],
        'Duration':[],
        'Popularity':[],
        'Release date':[],
        'Date added':[],
        'Artist id':[],
        'Track id':[],
        'Date loaded data':[]
    }

    #Append data:

    for item in tracks['tracks']['items']:
        tracks_df['Name'].append(check_data(item, ['track','name']))

        artist_check = check_data(item, ['track','artists'])

        if artist_check != 'No data':
            tracks_df['Artist'].append(check_data(artist_check[0], ['name'] ))
            tracks_df['Artist id'].append(check_data(artist_check[0],['id']))
        else:
            tracks_df['Artist'].append('No data')
            tracks_df['Artist id'].append('No data')
        
        tracks_df['Album'].append(check_data(item, ['track', 'album', 'name']))
        tracks_df['Genres'].append('No data')

        duration_ms = check_data(item, ['track', 'duration_ms'])
        if duration_ms != 'No data':
            duration = str(datetime.timedelta(milliseconds=duration_ms)).split('.')[0]
            tracks_df['Duration'].append(duration)
        else:
            tracks_df['Duration'].append('No data')
        
        tracks_df['Popularity'].append(check_data(item, ['track','popularity']))
        tracks_df['Release date'].append(check_data(item, ['track', 'album', 'release_date']))
        tracks_df['Date added'].append(check_data(item,['added_at']))
        tracks_df['Track id'].append(check_data(item, ['track', 'id']))
        tracks_df['Date loaded data'].append(str(datetime.date.today()))

    tracks_df = pd.DataFrame(tracks_df)
    
    tracks_df.drop_duplicates(keep='first')
    
    save_jason('tracks_transformed.json',tracks_df.to_dict(orient='list'))

    #Print Data frames for a preview

    print("Playlist songs: ")
    print()

    #Only print important information at this time

    print(tracks_df)
