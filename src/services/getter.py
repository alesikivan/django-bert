import pickle
from pathlib import Path
from src.parser_settings import TEST_ITEMS_COUNT, TO_LIMIT_ITEMS, SCENARIO_INIT

class Getter:

    @staticmethod
    def getContent():
        huge_data_update_format_pickle_path = Path('src/data/huge_data_update_format.pickle')
        with open(huge_data_update_format_pickle_path, 'rb') as pickle_file:
            content = pickle.load(pickle_file)

        # Slice items dict for fast testing
        if TO_LIMIT_ITEMS:
            content = dict(list(content.items())[:TEST_ITEMS_COUNT])

        return content

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
        huge_data_update_format_pickle_path = Path('src/data/collectioner_short_description.pickle')
        with open(huge_data_update_format_pickle_path, 'rb') as pickle_file:
            data = pickle.load(pickle_file)

        descriptions = []
        for _id in ids:
            descriptions.append({int(_id): data.get(str(_id))})

        return descriptions
