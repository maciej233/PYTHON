import glob, re
from graphviz import Digraph, Source

pattern = re.compile('Et[23]/[0123]')

device_lldp_neighbors = []

for file_name in glob.glob("/tmp/logi_lldp/*"):
    device = file_name.split("/")[3].split("_")[0]
    #print("device: " + device)
    with open(file_name, 'r') as f:
        for line in f.readlines():
            line = eval(line)  # EVAL LINE AS LIST
            for item in line[0]:
                # match pattern
                if re.search(pattern, item):
                    #print(" neighors: " + item.split()[0].split('.')[0])
                    device_lldp_neighbors.append((device, item.split()[0].split('.')[0]))
                    #print(device_lldp_neighbors)
print("*"*10)
print("Edges: " + str(device_lldp_neighbors))

my_graph = Digraph("My_Network")
my_graph.edge("Client", "s07")
my_graph.edge("s13", "Server")
my_graph.edge("s01", "r1")
my_graph.edge("r1", "r2")
my_graph.edge("r2", "s10")


# make neigbors edges for graph
for neighbors in device_lldp_neighbors:
    node1, node2 = neighbors
    my_graph.edge(node1, node2)

source = my_graph.source
original_text = "digraph My_Network {"
new_text = 'digraph My_Network {\n\
    {rank=same s01 r1 r2 s10}\n\
    {rank=same s02 s03 s04}\n\
    {rank=same s05 s06}\n\
    {rank=same Client s07 s08}\n\
    {rank=same s11 s12}\n'
new_source = source.replace(original_text, new_text)
print(new_source)
new_graph = Source(new_source)
new_graph.render("output/fourh_graph.gv")