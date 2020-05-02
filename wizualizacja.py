import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
import pylab


Robot = nx.OrderedDiGraph()
Ladowanie = nx.OrderedDiGraph()
Przybijanie = nx.OrderedDiGraph()
s1 = "Wozek\nwysuniety"
s2 = "Wozek\nwsuniety"
s3 = "Robot\ngotowy"
s4 = "Ladowanie"
s5 = "Przybijanie"
s6 = "Robot\npracuje"
s7 = "Pozycja A"
s8 = "Pozycja B"
s9 = "Alarm A"
s10 = "Alarm B"
s11 = "Zlap\nklocek"
s12 = "Przybij\nklocek"
s13 = "Pozycja\narsenal"
s14 = "Laduj\nzszywki"
s15 = "Alarm\nzszywki"
Robot.add_edges_from([(s1, s2), (s2, s1), (s2, s3), (s3, s2), (s3, s4), (s4,s3), (s3, s5), (s5,s3)])
Przybijanie.add_edges_from([(s5,s6),(s6,s7),(s6,s8),(s7,s9),(s9,s7),(s8,s10),(s10,s8),(s7,s11),(s8,s11),(s11,s12),(s12,s6)])
Ladowanie.add_edges_from([(s4,s13),(s13,s15),(s15,s13),(s13,s14),(s14,s13)])
# Robot.add_edges_from(Przybijanie.edges)
# Robot.add_edges_from(Ladowanie.edges)
#
#
# val_map = {'A': 1.0, 'D': 0.5714285714285714, 'H': 0.0}
#
# values = [val_map.get(node, 0.45) for node in G.nodes()]
# edge_labels = dict([((u, v,), d['weight'])
#                  for u, v, d in G.edges(data=True)])
# red_edges = [('tramwaj', 'D'), ('D', 'A')]
# edge_colors = ['black' if not edge in red_edges else 'red' for edge in G.edges()]
#
# pos = nx.spring_layout(Robot)
# pos = graphviz_layout(Robot, prog='dot')
# nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
nx.draw(Robot, node_size=4000, edge_cmap=plt.cm.Reds, with_labels=True, edge_color='black', node_color='blue')
pylab.show()
nx.draw(Przybijanie, node_size=4000, edge_cmap=plt.cm.Reds, with_labels=True, edge_color='black', node_color='green')
pylab.show()
nx.draw(Ladowanie, node_size=4000, edge_cmap=plt.cm.Reds, with_labels=True, edge_color='black', node_color='red')
pylab.show()
