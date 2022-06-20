import networkx as nx
import numpy as np

class Describer:

    #characteristic words of each community
    @staticmethod
    def describePartition(W2, MC, partition, H = 0):
        deg = dict(W2.degree())
        totDegree = sum(list(deg.values()))
        N = len(W2)
        for c in range(MC[H]):
            cind = [n for n in partition[H].keys() if partition[H][n]==c] #community nodes
            WC = W2.subgraph(cind) #community subgraph
            degc = dict(WC.degree())
            NC = len(WC)
            #commDegree = sum(list(degc.values()))
            predpower = np.zeros(len(cind))
            for i in range(len(cind)):
                n = cind[i]
                d = (deg[n] + (deg[n] == 0))
                p1 = degc[n] / d; p2 = (NC - degc[n]) / (N - d)
                predpower[i] = degc[n] * np.log(p1) + (NC - degc[n]) * np.log(p2) + \
                               (d - degc[n]) * np.log(1.00001 - p1) + (N - NC - d + degc[n]) * np.log(1.0001 - p2)
            topwordind = np.argsort(predpower)[-10:][::-1] #top words of the community by degree
            print('Community {:d}: {:d} words'.format(c, len(cind)))
            print('Characteristic words: ', [cind[i] for i in topwordind])

    #characteristic words of focus area
    @staticmethod
    def describeFocusArea(content, W, focus_area, X2, X):
        focus_mask = (X2[:, 1] > focus_area[0][0]) & (X2[:, 1] < focus_area[0][0] + focus_area[1][0]) & (X2[:, 2] > focus_area[0][1]) & (X2[:, 2] < focus_area[0][1] + focus_area[1][1])
        focus_ids = X[focus_mask, 0]
        __class__.describeFocusIds(content, W, focus_ids, 2)


    def describeFocusIds(content, W, focus_ids, version):
        focus_ids = [int(i) for i in focus_ids]
        if (version == 1):
            focus_ids_string = [str(i) for i in focus_ids]

        if (version == 2):
            focus_ids_string = focus_ids

        if (version == 3):
            focus_ids_string = focus_ids


        WR = nx.DiGraph() #bi-partite graph of resources to words
        WF = nx.DiGraph()
        vocab = {}
        for k in content.keys():
            c = content.get(k)
            for i in range(len(c)):
                for w in c[i]:
                    if WR.has_edge(k, w):
                        WR[k][w]['weight'] += 1
                    else:
                        WR.add_edge(k, w, weight = 1)

        for k in focus_ids_string:
            c = content.get(k)
            for i in range(len(c)):
                for w in c[i]:
                    vocab[w] = vocab.get(w,0) + 1
                    if WF.has_edge(k, w):
                            WF[k][w]['weight'] += 1
                    else:
                            WF.add_edge(k, w, weight = 1)

        #WF = WR.subgraph(list(W.nodes()) + focus_ids_string)

        #characteristic words of each community
        deg = dict(WR.in_degree())
        N = len(content.keys())
        degc = dict(WF.in_degree())
        NC = len(focus_ids_string)
        allwords = list(W.nodes())
        focuswords = list(vocab.keys())
        #focuswords = list(set(WF.nodes()) - set(focus_ids_string))
        predpower = np.zeros(len(focuswords))
        for i in range(len(focuswords)):
                n = focuswords[i]
                
                d = deg[n]
                if (d == 0):
                    d = 1

                p1 = degc[n] / d + 0.0001 * (degc[n] == 0)


                N_minus_d = N - d
                if (N_minus_d == 0):
                    N_minus_d = 1

                p2 = (NC - degc[n]) / N_minus_d + 0.0001 * (NC == degc[n])

                predpower[i] = degc[n] * np.log(p1) + (NC - degc[n]) * np.log(p2) + \
                               (d - degc[n]) * np.log(1.00001 - p1) + (N - NC - d + degc[n]) * np.log(1.0001 - p2)
                #predpower[i] = degc[n]
                if np.isnan(predpower[i]):
                    predpower[i] = -np.inf

        topwordind = np.argsort(predpower)[-10:][::-1] #top words of the community by degree
        print('Focus area: {:d} resources'.format(len(focus_ids)))

        words = [focuswords[i] for i in topwordind]
        print('Characteristic words: ', words)

        return words
