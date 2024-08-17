print("Starting KnowledgeGraphed...")

import networkx
import spacy
import pickle

nlp = spacy.load('en_core_web_sm')

print("KnowledgeGraphed v0.1.0 (c) Craig Giles 2024")
print("------------\n")

filename = input("Name of text file: ")

with open(filename, "r") as f:
    doc = nlp(f.read())

graph = networkx.graphml.read_graphml("graph.graphml")

with open("node_count.txt", "r") as f:
    counter = int(f.read())

local_counter = 0

for chunk in doc.noun_chunks:
    graph.add_node(chunk.text)
    if not local_counter == 0:
        graph.add_edge(list(graph.nodes)[counter-1], chunk.text, data=chunk.root.head.text)
    counter += 1
    local_counter += 1

print("Knowledge", graph, "created!")

with open("node_count.txt", "w") as f:
    f.write(str(counter))

networkx.graphml.write_graphml_lxml(graph, "graph.graphml")