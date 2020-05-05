import networkx as nx
import numpy as np
from networkx.drawing.nx_agraph import write_dot, graphviz_layout, to_agraph
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import pylab


Robot = nx.MultiDiGraph()
Ladowanie = nx.MultiDiGraph()
Przybijanie = nx.MultiDiGraph()
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
Robot.add_edges_from([(s1, s2),(s1,s1), (s2, s1), (s2, s3), (s3, s2), (s3, s4), (s4,s3), (s3, s5), (s5,s3),(s3,s3)])
Przybijanie.add_edges_from([(s5,s6),(s6,s5),(s6,s7),(s6,s8),(s7,s9),(s9,s7),(s9,s9),(s10,s10),(s8,s10),(s10,s8),(s7,s11),(s8,s11),(s11,s12),(s12,s6)])
Ladowanie.add_edges_from([(s4,s13),(s13,s4),(s13,s15),(s15,s13),(s15,s15),(s13,s14),(s14,s13)])
Robot.add_edges_from(Przybijanie.edges)
Robot.add_edges_from(Ladowanie.edges)


list = list(Robot)


def check_block():
    blockades = False
    for i in range(len(list)):
        for j in range(len(list)):
            source = list[i]
            target = list[j]
            is_path = nx.has_path(Robot, source=source, target=target)
            source.replace('\n', ' ')
            target.replace('\n', ' ')
            if not is_path:
                print("Jest blokada miedzy " + source + " a " + target)
                blockades = True
                break
    if not blockades:
        print("Brak blokad")


def show_path(source, target):
    for i in range(len(list)):
        for j in range(len(list)):
            is_path = nx.has_path(Robot, source=source, target=target)
            path = nx.shortest_path(Robot, source=source, target=target)
            if not is_path:
                print("NO PATH")
                break
    for k in range(len(path)):
        path[k] = path[k].replace('\n', ' ')
    print(path)

check_block()
show_path(s7,s8)

Robot.graph['edge'] = {'arrowsize': '0.6', 'splines': 'curved'}
Robot.graph['graph'] = {'scale': '4'}
Graf = to_agraph(Robot)
Graf.layout('dot')
Graf.draw('Graf.png')
img = mpimg.imread('Graf.png')
imgplot = plt.show(img)
# plt.axis('off')
# plt.show(imgplot)