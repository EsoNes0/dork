# -*- coding: utf-8 -*-
"""Generates map from yaml data
"""

from pprint import pprint
import networkx as nx
import yaml
import matplotlib.pyplot as plt


CARDINALS = ["north", "east", "south", "west"]


def load_data(file_name_and_path="./dork/dork.yml"):
    """Loads data from yaml file into data"""
    with open(file_name_and_path) as file:
        data = yaml.safe_load(file.read())

    return data


def convert_dict_edges():
    """Convert Dictionary to edges"""
    data = load_data()
    edges = []
    rooms = data["Rooms"]
    for name in rooms:
        room = rooms[name]
        for direction in CARDINALS:
            if direction in room and room[direction]is not None:
                edges.append((room[direction], name))
    return edges


def convert_dict_nodes():
    """Convert Dictionary to Nodes"""
    data = load_data()
    nodes = []
    rooms = data["Rooms"]
    for name in rooms:
        nodes.append(name)
    return nodes


def generate_map():
    """Returns a map from the nodes and edges lists"""
    nodes = convert_dict_nodes()
    edges = convert_dict_edges()
    if nodes and edges:
        nx.empty_graph()
        map_graph = nx.Graph()
        map_graph.add_nodes_from(nodes)
        map_graph.add_edges_from(edges)
        # nx.draw(map_graph, with_labels=True)
        plt.show()
        return map_graph
    return print("Error in map generation")


# def _check_path():
#     data = load_data()
#     rooms = data["Rooms"]
#     room = rooms[name]
#     if direction not in room:
#         print(f"{name} does not have {direction} as a key.")
#     elif room[direction] is None:
#         print(f"There is nothing {direction} of {name}.")
#     elif room[direction] not in rooms:
#         print(f"Going {direction} of {name} leads to an error!")
#     else:
#         other = room[direction]
#         print(f"{other} is {direction} of {name}")


def check_data(data):
    """Tests yaml file to see if it is a correct format"""
    print("\nChecking that 'data' contains a dictionary of rooms... \n")
    if "Rooms" not in data:
        print("No Rooms found.")
        return False

    if not isinstance(data["Rooms"], dict):
        print("Rooms in data was not proper data.")
        return False

    print("Rooms found with proper data.\n")
    return True


def main():
    """Runnable main of map_generator, requires correctly formatted yaml file,
    returns"""
    data = load_data()
    print("loaded this data: ")
    pprint(data)
    print(convert_dict_nodes())

    if check_data(load_data()):
        generate_map()
        # _check_path()


if __name__ == "__main__":
    main()
