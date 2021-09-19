
from dotenv import load_dotenv
from pymongo import MongoClient

from good_songs import insert_good_songs
load_dotenv()


def __main__():
    client = MongoClient('mongodb://localhost:27017/')

    insert_good_songs(client=client)

    # insert_bad_songs(client=client)


if __name__ == '__main__':
    __main__()