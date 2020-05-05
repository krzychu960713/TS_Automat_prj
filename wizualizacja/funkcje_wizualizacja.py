import networkx as nx


def check_block(Robot):
    lists = list(Robot)
    blockades = False
    for i in range(len(lists)):
        for j in range(len(lists)):
            source = lists[i]
            target = lists[j]
            is_path = nx.has_path(Robot, source=source, target=target)
            source.replace('\n', ' ')
            target.replace('\n', ' ')
            if not is_path:
                print("Jest blokada miedzy " + source + " a " + target)
                blockades = True
                break
    if not blockades:
        print("Brak blokad")


def show_path(Robot, source, target):
    lists = list(Robot)
    for i in range(len(lists)):
        for j in range(len(lists)):
            is_path = nx.has_path(Robot, source=source, target=target)
            path = nx.shortest_path(Robot, source=source, target=target)
            if not is_path:
                print("NO PATH")
                break
    for k in range(len(path)):
        path[k] = path[k].replace('\n', ' ')
    print(path)