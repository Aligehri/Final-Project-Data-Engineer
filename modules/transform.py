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

def transform_data():

    recently = read_json('recently.json')
    top_tracks = read_json('top_tracks.json')
    top_artists = read_json('top_artists.json')

    #Create dicts to append data:

    recently_df = {
        'Track name':[],
        'Artist':[], 
        'Album':[], 
        'Duration h:m:s':[],
        'Day played':[], 
        'Time played':[],
        'Release date':[],
        'Track popularity':[],
        'Track id':[],
        'Artist id':[],
        'Date loaded data':[]
        }

    top_tracks_df = {
        'Track name':[], 
        'Artist':[], 
        'Album':[],  
        'Duration h:m:s':[], 
        'Release date':[], 
        'Popularity':[], 
        'Track id':[],
        'Date loaded data':[]
        }

    top_artists_df = {
        'Artist':[],
        'Followers':[],
        'Genres':[],
        'Popularity':[],
        'Artist id':[],
        'Date loaded data':[]
    }

    #Append data:

    for item in recently['items']:
        recently_df['Track name'].append(check_data(item, ['track', 'name']))

        artist_check = check_data(item, ['track','artists'])
        if artist_check != 'No data':
            recently_df['Artist'].append(check_data(artist_check[0], ['name'] ))
            recently_df['Artist id'].append(check_data(artist_check[0],['id']))
        else:
            recently_df['Artist'].append('No data')
            recently_df['Artist id'].append('No data')

        recently_df['Album'].append(check_data(item, ['track', 'album', 'name']))
        
        duration_ms = check_data(item, ['track', 'duration_ms'])
        if duration_ms != 'No data':
            duration = str(datetime.timedelta(milliseconds=duration_ms)).split('.')[0]
            recently_df['Duration h:m:s'].append(duration)
        else:
            recently_df['Duration h:m:s'].append('No data')

        recently_df['Day played'].append(check_data(item, ['played_at'])[0:10])
        recently_df['Time played'].append(check_data(item, ['played_at'])[11:22])
        recently_df['Release date'].append(check_data(item, ['track', 'album', 'release_date']))
        recently_df['Track popularity'].append(check_data(item, ['track', 'popularity']))
        recently_df['Track id'].append(check_data(item, ['track', 'id']))
        recently_df['Date loaded data'].append(str(datetime.date.today()))

    

    for item in top_tracks['items']:
        top_tracks_df['Track name'].append(check_data(item,['name']))

        artist_check = check_data(item, ['artists'])
        if artist_check != 'No data':
            top_tracks_df['Artist'].append(check_data(artist_check[0],['name']))
        else:
            recently_df['Artist'].append('No data')
        
        top_tracks_df['Album'].append(check_data(item,['album','name']))

        duration_ms = check_data(item, ['duration_ms'])
        if duration_ms != 'No data':
            duration = str( datetime.timedelta(milliseconds=duration_ms)).split('.')[0]
            top_tracks_df['Duration h:m:s'].append(duration)
        else:
            top_tracks_df['Duration h:m:s'].append('No data')
        
        top_tracks_df['Release date'].append(check_data(item,['album', 'release_date']))
        top_tracks_df['Popularity'].append(check_data(item,['popularity']))
        top_tracks_df['Track id'].append(check_data(item,['id']))
        top_tracks_df['Date loaded data'].append(str(datetime.date.today()))

    

    for item in top_artists['items']:
        top_artists_df['Artist'].append(check_data(item,['name']))
        top_artists_df['Followers'].append(check_data(item,['followers', 'total']))
        
        genres_check = check_data(item,['genres'])
        if genres_check != 'No data':
            top_artists_df['Genres'].append(', '.join(genres_check))
        else:
            top_artists_df['Genres'].append('No data')
        
        top_artists_df['Popularity'].append(check_data(item,['popularity']))
        top_artists_df['Artist id'].append(check_data(item,['id']))
        top_artists_df['Date loaded data'].append(str(datetime.date.today()))

    

    save_jason('recently_transformed.json',recently_df)
    save_jason('top_tracks_transformed.json',top_tracks_df)
    save_jason('top_artists_transformed.json', top_artists_df)

    recently_df = pd.DataFrame(recently_df)
    top_tracks_df = pd.DataFrame(top_tracks_df)
    top_artists_df = pd.DataFrame(top_artists_df)

    #Print Data frames for a preview

    print("Recently played songs: ")
    print()

    #Only print important information at this time

    print(recently_df[['Track name', 'Artist', 'Album', 'Duration h:m:s', 'Day played', 'Time played']])
    print()
    print()
    print("Your top 50 songs:")
    print()
    print(top_tracks_df)
    print()
    print()
    print("Your top 50 artists:")
    print()
    print(top_artists_df)