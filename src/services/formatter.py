import pickle
import numpy as np
from pathlib import Path
from src.parser_settings import TEST_ITEMS_COUNT, TO_LIMIT_ITEMS, SCENARIO_INIT

class Formatter:

    @staticmethod
    def format():
        pickle_file_path = Path('src/data/abstracts2_projection2d.pickle')

        with open(pickle_file_path, 'rb') as pickle_file:
            coordinates = pickle.load(pickle_file)

        return coordinates
