import pickle
import networkx as nx
from pathlib import Path
from src.parser_settings import TEST_ITEMS_COUNT, TO_LIMIT_ITEMS, SCENARIO_INIT

class GraphHandler:

    def __init__(self, degT):
        self.degT = degT

    def make_hierarchy(self):
        hierarchy_deg_pickle_path = Path('src/data/hierarchy_deg{}.pickle'.format(self.degT))
        if SCENARIO_INIT: #construct and partition word graph unless saved

            #create graph of all words
            W = nx.Graph()
            for key in content:
                c = content.get(key)
                for i in range(len(c)):
                    for j in range(len(c[i]) - 1):
                        if W.has_edge(c[i][j], c[i][j + 1]):
                            W[c[i][j]][c[i][j + 1]]['weight'] += 1
                        else:
                            W.add_edge(c[i][j], c[i][j + 1], weight = 1)


            #remove '.' apparently

            #sample the graph, pick only frequent words
            deg = dict(W.degree())
            W2 = W.subgraph([d for d in deg.keys() if deg[d]>=degT])

            partitioner = Partitioner(degT)
            (partition, MC) = partitioner.hierPart(W2, last_partition_level = 3)

            #np.unique(np.array(list(partition.values())), axis = 0)

            with open(hierarchy_deg_pickle_path, 'wb') as pickle_file2:
                pickle.dump([W, W2, MC, partition], pickle_file2)
        else:
            with open(hierarchy_deg_pickle_path, 'rb') as pickle_file2:
                [W, W2, MC, partition] = pickle.load(pickle_file2)

        return [W, W2, MC, partition]
