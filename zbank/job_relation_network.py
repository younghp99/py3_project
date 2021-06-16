# -*- coding: utf-8 -*-
'''
@author: hp
'''
import networkx as nx
import matplotlib.pyplot as plt
G = nx.DiGraph()
G.add_node('start')
G.add_nodes_from([3, 4, 5, 6])
G.add_edge('start', 3)
G.add_edges_from([(3, 5), (3, 6), (6, 7)],color='red')
print("输出全部节点：{}".format(G.nodes()))
print("输出全部边：{}".format(G.edges()))
print("输出全部边的数量：{}".format(G.number_of_edges()))
nx.draw(G,with_labels=True)
plt.show()