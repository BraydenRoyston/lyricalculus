from dotenv import load_dotenv
from pymongo import MongoClient
from get_data import insert_raw_data
from add_features import add_features
import sys

load_dotenv()


def main():
    client = MongoClient('mongodb://localhost:27017/')

    if(len(sys.argv) > 1 and sys.argv[1] == "--reset"):
        insert_raw_data(client=client)

    add_features(client=client)


if __name__ == "__main__":
    main()