# pip install matplotlib networkx

import matplotlib.pyplot as plt
import networkx as nx
from rdflib import Graph, Namespace, RDF, Literal, URIRef


def load_rdf_graph(file_path):
    g = Graph()
    g.parse(file_path, format='xml')
    return g

def visualize_graph(graph, output_file):
    G = nx.DiGraph()

    for s, p, o in graph:
        subject_label = str(s).split("/")[-1]
        object_label = str(o).split("/")[-1] if isinstance(o, URIRef) else o

        G.add_node(subject_label)
        G.add_node(object_label)
        G.add_edge(subject_label, object_label, label=str(p).split("/")[-1])

    pos = nx.spring_layout(G)
    labels = nx.get_edge_attributes(G, 'label')

    nx.draw(G, pos, with_labels=True, font_weight='bold', node_color='skyblue', node_size=1000, arrowsize=20)
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)

    plt.savefig(output_file)
    plt.show()

def visualize_relation(graph, node_id, output_file):
    G = nx.DiGraph()

    G.add_node(node_id, label=node_id)

    for s, p, o in graph.triples((Namespace("http://example.org/friends/")[node_id], None, None)):
        object_label = str(o).split("/")[-1] if isinstance(o, URIRef) else o
        G.add_node(object_label)
        G.add_edge(node_id, object_label, label=str(p).split("/")[-1])

    pos = nx.spring_layout(G)
    labels = nx.get_edge_attributes(G, 'label')

    nx.draw(G, pos, with_labels=True, font_weight='bold', node_color='skyblue', node_size=1000, arrowsize=20)
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)

    plt.savefig(output_file)
    plt.show()

def visualize_relation_by_name(graph, friend_name, output_file):
    G = nx.DiGraph()

    friend_ns = Namespace("http://example.org/friends/")

    # Find the friend's ID based on the name
    friend_id = None
    for s, p, o in graph.triples((None, Namespace("http://example.org/friends/").name, Literal(friend_name))):
        friend_id = str(s).split("/")[-1]

    if friend_id is not None:
        G.add_node(friend_id, label=friend_name)

        for s, p, o in graph.triples((friend_ns[friend_id], None, None)):
            object_label = str(o).split("/")[-1] if isinstance(o, URIRef) else o
            G.add_node(object_label)
            G.add_edge(friend_id, object_label, label=str(p).split("/")[-1])

        plt.figure(num=f'{friend_name} relations by name in GRAPH')
        pos = nx.spring_layout(G)
        labels = nx.get_edge_attributes(G, 'label')

        nx.draw(G, pos, with_labels=True, font_weight='bold', node_color='skyblue', node_size=1000, arrowsize=20)
        nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)

        plt.savefig(output_file)
        plt.show()
    else:
        print(f"Friend with name '{friend_name}' not found in the graph.")

def show_relations_for_multiple_friends(graph, friend_names):
    for friend_name in friend_names:
        output_file = f'graph_images/{friend_name.lower()}_relations.png'
        visualize_relation_by_name(graph, friend_name, output_file)


def visualize_relations_for_friends(graph, friend_names, output_file):
    G = nx.DiGraph()

    friend_ns = Namespace("http://example.org/friends/")

    # Add nodes for each friend
    for friend_name in friend_names:
        friend_id = None
        for s, p, o in graph.triples((None, friend_ns.name, Literal(friend_name))):
            friend_id = str(s).split("/")[-1]

        if friend_id is not None:
            G.add_node(friend_id, label=friend_name)

            for s, p, o in graph.triples((friend_ns[friend_id], None, None)):
                object_label = str(o).split("/")[-1] if isinstance(o, URIRef) else o
                G.add_node(object_label)
                G.add_edge(friend_id, object_label, label=str(p).split("/")[-1])
        else:
            print(f"Friend with name '{friend_name}' not found in the graph.")

    # Draw the graph
    plt.figure(num=f'Relations for Friends: {", ".join(friend_names)}')
    pos = nx.spring_layout(G)
    labels = nx.get_edge_attributes(G, 'label')

    nx.draw(G, pos, with_labels=True, font_weight='bold', node_color='skyblue', node_size=1000, arrowsize=20)
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)

    plt.savefig(output_file)
    plt.show()

# Example usage:



# Example usage:
rdf_graph = load_rdf_graph('friends.rdf')
# visualize_graph(rdf_graph, 'graph_images/all_relations.png')
# visualize_relation(rdf_graph, '1', 'graph_images/alice_relations.png')
# visualize_relation_by_name(rdf_graph, 'Alice', 'graph_images/alice_relations_by_name.png')

friends_to_show_single = ['Alice', 'Charlie', 'Ivan', 'Frank']
# show_relations_for_multiple_friends(rdf_graph, friends_to_show_single)

friends_to_show = ['Alice', 'Charlie', 'Ivan', 'Frank']
output_file = 'graph_images/multiple_friends_relations.png'
visualize_relations_for_friends(rdf_graph, friends_to_show, output_file)


