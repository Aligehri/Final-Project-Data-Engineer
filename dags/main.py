from modules import extract_data, transform_data, load_data
from decouple import config

def main():
    extract_data()

    transform_data()

    load_data()

if __name__ == '__main__':
    main()