# use graphviz to draw neural network

import pygraphviz as pgv

labels_dict = {0: "3x3 conv", 1: "3x3 sep-conv", 2: "5x5 conv",
               3: "5x5 sep-conv", 4: "avg_pooling", 5: "max_pooling",
               -1: "input", -2: "output"}


def add_node(graph, id, type, shape='box', style='filled'):
    label = labels_dict[type]
    if type == 0:
        color = 'seagreen3'
    elif type == 1:
        color = 'skyblue'
    elif type == 2:
        color = 'greenyellow'
    elif type == 3:
        color = 'yellow'
    elif type == 4:
        color = 'pink'
    elif type == 5:
        color = 'orange'
    elif type == 6:
        color = 'greenyellow'
    else:
        color = 'white'

    graph.add_node(id, label=label, color='black', fillcolor=color, shape=shape, style=style)


def draw_network(network):
    graph = pgv.AGraph(directed=True, strict=True, fontname='Helvetica', arrowtype='open')

    for id, type in enumerate(network):
        add_node(graph, id, type)
        if id + 1 != len(network):
            graph.add_edge(id, id + 1)
        # graph.add_edge(id, id+1, style='dotted')
    # neato, dot, twopi, circo, fdp, nop, wc, acyclic, gvpr, gvcolor, ccomps, sccmap, tred, sfdp, unflatten.
    graph.layout(prog='circo')
    graph.draw("./network.png")


if __name__ == '__main__':
    network = [-1, 0, 3, 5, 1, 4, 2, -2]
    draw_network(network)
