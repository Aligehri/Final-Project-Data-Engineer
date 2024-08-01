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
        'Artist id':[]
        }

    top_tracks_df = {
        'Track name':[], 
        'Artist':[], 
        'Album':[],  
        'Duration h:m:s':[], 
        'Release date':[], 
        'Popularity':[], 
        'Track id':[] 
        }

    top_artists_df = {
        'Artist':[],
        'Followers':[],
        'Genres':[],
        'Popularity':[],
        'Artist id':[]
    }

    #Append data:

    for item in recently['items']:
        recently_df['Track name'].append(item['track']['name'])
        recently_df['Artist'].append(item['track']['artists'][0]['name'])
        recently_df['Album'].append(item['track']['album']['name'])
        recently_df['Duration h:m:s'].append( str( datetime.timedelta(milliseconds=item['track']['duration_ms'])).split('.')[0])
        recently_df['Day played'].append(item['played_at'][0:10])
        recently_df['Time played'].append( item['played_at'][11:22] )
        recently_df['Release date'].append( item['track']['album']['release_date'] )
        recently_df['Track popularity'].append (item['track']['popularity'])
        recently_df['Track id'].append( item['track']['id'] )
        recently_df['Artist id'].append( item['track']['artists'][0]['id'] )

    save_jason('recently_transformed.json',recently_df)

    for item in top_tracks['items']:
        top_tracks_df['Track name'].append(item['name'])
        top_tracks_df['Artist'].append(item['artists'][0]['name'])
        top_tracks_df['Album'].append(item['album']['name'])
        top_tracks_df['Duration h:m:s'].append( str( datetime.timedelta(milliseconds=item['duration_ms'])).split('.')[0])
        top_tracks_df['Release date'].append(item['album']['release_date'])
        top_tracks_df['Popularity'].append(item['popularity'])
        top_tracks_df['Track id'].append(item['id'])

    save_jason('top_tracks_transformed.json',top_tracks_df)

    for item in top_artists['items']:
        top_artists_df['Artist'].append(item['name'])
        top_artists_df['Followers'].append(item['followers']['total'])
        top_artists_df['Genres'].append(', '.join(item['genres']))
        top_artists_df['Popularity'].append(item['popularity'])
        top_artists_df['Artist id'].append(item['id'])

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