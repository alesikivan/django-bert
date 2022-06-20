import pickle
import pycombo
import numpy as np

from pathlib import Path
from src.parser_settings import TEST_ITEMS_COUNT, TO_LIMIT_ITEMS, SCENARIO_INIT 

class Partitioner:

    def __init__(self, degT):
        self.degT = degT

    def hierPart(self, graph, last_partition_level = 1):

        partition = self.getPartition(graph)

        communities_amounts = np.zeros(last_partition_level, dtype = int) # number of communities at each level
        communities_amounts[0] = max(partition[0].values()) + 1

        for partition_level in range(1, last_partition_level):
            
            partition[partition_level] = {}
            communities_amounts[partition_level] = 0
            
            for communities_amount_on_level in range(communities_amounts[partition_level-1]):
                print('Hier {}, comm {}'.format(partition_level, communities_amount_on_level))
                try:
                    cind = [
                        n for n in partition[partition_level-1].keys() 
                        if partition[partition_level-1][n] == communities_amount_on_level
                    ]

                    GC = graph.subgraph(cind)
                    if len(GC) >= 3:
                        print('- - Ready to partition, {} nodes'.format(len(GC)))
                        cPart = pycombo.execute(GC)[0]
                        print('- - Partition complete')
                    else:
                        print('- - Partition skipped, {} nodes'.format(len(GC)))
                        cPart = {n : 0 for n in GC.nodes()}
                    for n in cind:
                        partition[partition_level][n] = cPart[n] + communities_amounts[partition_level]
                    communities_amounts[partition_level] = max(list(partition[partition_level].values())) + 1
                except:
                    1 == 1

        return (partition, communities_amounts)


    def getPartition(self, graph):
        partition_deg_path = Path('src/data/partition_deg{}.pickle'.format(self.degT))
        
        if SCENARIO_INIT:
            partition = {0: pycombo.execute(graph)[0]} # upper level partition
            with open(partition_deg_path, 'wb') as pickle_file:
                pickle.dump([partition], pickle_file)
        else:
            with open(partition_deg_path, 'rb') as pickle_file:
                [partition] = pickle.load(pickle_file)

        return partition