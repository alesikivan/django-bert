import json

from src.services.describer import Describer
from src.services.drawer import Drawer
from src.services.partitioner import Partitioner
from src.services.getter import Getter
from src.services.graph_handler import GraphHandler
from src.services.formatter import Formatter

from src.parser_settings import TEST_ITEMS_COUNT, TO_LIMIT_ITEMS, SCENARIO_INIT, DEG_T

class MainHandler:

	@staticmethod
	def get_ids_description(focus_ids):
		content = Getter.getContent()

		graph_handler = GraphHandler(DEG_T)
		[W, W2, MC, partition] = graph_handler.make_hierarchy()

		words = Describer.describeFocusIds(content, W, focus_ids, 1)
		return words

	# @staticmethod
	# def get_data():
	# 	graph_handler = GraphHandler(DEG_T)
	# 	content = Getter.getContent()
	#
	# 	[W, W2, MC, partition] = graph_handler.make_hierarchy()
	# 	[X, X2] = Formatter.original_format(MC, content)
	#
	# 	return X2.tolist()

	@staticmethod
	def get_data():
		coordinates = Formatter.format()
		return coordinates.tolist()

	@staticmethod
	def get_ids_links(ids):
		return Getter.getLinks(ids)

	@staticmethod
	def get_ids_short_descriptions(ids):
		return Getter.getShortDescriptions(ids)
