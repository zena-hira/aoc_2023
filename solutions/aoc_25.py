import networkx as nx
import math

def one(lines):

    G = nx.Graph()

    for line in lines:
        ws = line.split(' ')
        first = ws[0][0:-1]
        for r in ws[1:]:
            G.add_edge(first, r)

    cuts = nx.minimum_edge_cut(G)

    for e in cuts:
        G.remove_edge(e[0], e[1])

    return math.prod([len(c) for c in nx.connected_components(G)])

