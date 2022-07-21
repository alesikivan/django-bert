import pickle
import numpy as np
import pandas as pd
from pathlib import Path
from src.parser_settings import TEST_ITEMS_COUNT, TO_LIMIT_ITEMS, SCENARIO_INIT
from sklearn.cluster import KMeans
from src.services.helper import ConvexHull2D, clockwise_sort

class Formatter:

    @staticmethod
    def get_cluster_data(ident):
        CLUSTERS_FILE = Path('src/data/bert/clusters_embeddings.csv')

        cols = [
            'ID',
            'Keywords',
            'emb_2d_0',
            'emb_2d_1',
            'borders'
        ]

        clusters_data = pd.read_csv(CLUSTERS_FILE, usecols=cols)

        return clusters_data\
            .loc[clusters_data['ID'] == ident][cols]\
            .to_numpy()\
            .flatten()\
            .tolist()

    @staticmethod
    def get_cluster_coordinates(ident):
        EMBEDDINGS_FILE = Path('src/data/bert/docs_embeddings.csv')

        cols = ['ID', 'emb_2d_0', 'emb_2d_1', 'topic_id']

        embeddings_data = pd.read_csv(EMBEDDINGS_FILE, usecols=cols)

        cols = ['ID', 'emb_2d_0', 'emb_2d_1']

        return embeddings_data\
            .loc[embeddings_data['topic_id'] == ident][cols]\
            .to_numpy()\
            .tolist()


    @staticmethod
    def format(file, coordinates_amount):
        with open(file, 'rb') as pickle_file:
            [X, coordinates, Y2, idCat] = pickle.load(pickle_file)

            amount = coordinates_amount or len(coordinates)
            coordinates = coordinates[:amount]

            # Temporary delete id (zero index)
            arr = np.delete(coordinates, 0, 1)
            arr = np.array(arr)

            return arr
