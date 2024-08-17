import networkx
import io
import matplotlib.pyplot as plot
import matplotlib.image as img

print("KnowledgeGraphed Viewer v0.1.0 (c) Craig Giles 2024")
print("------------\n")

graph = networkx.graphml.read_graphml("graph.graphml")
pydot_graph = networkx.drawing.nx_pydot.to_pydot(graph)


png_str = pydot_graph.create_png()
image = img.imread(io.BytesIO(png_str))


# plot the image
imgplot = plot.imshow(image)
plot.show()