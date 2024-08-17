print("Starting KnowledgeGraphed...")

import networkx
import spacy

nlp = spacy.load('en_core_web_sm')
graph = networkx.Graph()

print("KnowledgeGraphed v0.1.0 (c) Craig Giles 2024")
print("------------\n")

filename = input("Name of text file: ")

with open(filename, "r") as f:
    doc = nlp(f.read())

counter=0

for chunk in doc.noun_chunks:
    graph.add_node(chunk.text)
    if not counter == 0:
        graph.add_edge(list(graph.nodes)[counter-1], chunk.text, data=chunk.root.head.text)
    counter += 1

print("Knowledge", graph, "created!")

networkx.graphml.write_graphml_lxml(graph, "graph.graphml")