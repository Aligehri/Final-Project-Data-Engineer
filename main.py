from modules import extract_data, transform_data, load_data
from decouple import config

def main():
    #spotify credential:

    SPOTIPY_CLIENT_ID=config('SPOTIPY_CLIENT_ID')
    SPOTIPY_CLIENT_SECRET=config('SPOTIPY_CLIENT_SECRET')
    SPOTIPY_REDIRECT_URI = config('SPOTIPY_REDIRECT_URI')
    
    #Redshift credentials:
    
    user_rs = config('user_rs')
    pass_rs = config('pass_rs')
    host_rs = config('host_rs')
    port_rs = config('port_rs')
    database_rs = config('database_rs')
    schema = config('schema')

    extract_data(SPOTIPY_CLIENT_ID, SPOTIPY_CLIENT_SECRET, SPOTIPY_REDIRECT_URI)

    transform_data()

    load_data(user_rs, pass_rs, host_rs, port_rs, database_rs,schema)

if __name__ == '__main__':
    main()