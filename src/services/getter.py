import pandas as pd
import pickle
from pathlib import Path
from src.parser_settings import TEST_ITEMS_COUNT, TO_LIMIT_ITEMS, SCENARIO_INIT
from src.services.formatter import Formatter

class Getter:

    @staticmethod
    def get_content(params):
        CLUSTERS_FILE = Path('src/data/bert/clusters_embeddings.csv')
        clusters_cols = [
            'ID',
            'Keywords',
            'emb_2d_0',
            'emb_2d_1',
            'borders'
        ]

        clusters_data = pd.read_csv(CLUSTERS_FILE, usecols=clusters_cols)

        clusters = []

        clusters_amount = clusters_data['ID'].tolist()
        for ident in clusters_amount:
            [_id, keywords, x, y, borders] = Formatter.get_cluster_data(ident)

            cluster = {
                # 'documents': Formatter.get_cluster_coordinates(ident),
                'keywords': keywords,
                'borders': borders,
                'centroid': [x, y]
            }

            clusters.append(cluster)

        return clusters


    @staticmethod
    def get_coordinates(params):
        coordinates_amount = int( params.get('coordinates') or 1000 )

        pickle_file = Path('src/data/test/abstracts1_BERT.pickle')
        coordinates = Formatter.format(pickle_file, coordinates_amount)

        return coordinates.tolist()


    @staticmethod
    def getLinks(ids):
        huge_data_update_format_pickle_path = Path('src/data/collectioner_links.pickle')
        with open(huge_data_update_format_pickle_path, 'rb') as pickle_file:
            data = pickle.load(pickle_file)

        links = []
        for _id in ids:
            links.append({int(_id): data.get(str(_id))})

        return links

    @staticmethod
    def getShortDescriptions(ids):
        huge_data_update_format_pickle_path = Path('src/data/test/short_description.pickle')
        with open(huge_data_update_format_pickle_path, 'rb') as pickle_file:
            data = pickle.load(pickle_file)

        descriptions = []
        for _id in ids:
            descriptions.append({int(_id): data.get(str(_id))})

        return descriptions
