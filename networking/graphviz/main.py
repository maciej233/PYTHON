from graphviz import Digraph, Source
import glob, re

pattern = re.compile("Eth [0123]/[0123]")

device_cdp_neighbors = []

# gather inofmation about neighboring devices
for file_name in glob.glob("/home/maciej/repo/networking/graphviz/cdp_example_output/*"):
    path_length = len(file_name.split("/"))
    device = file_name.split("/")[path_length-1].split("_")[0]
    #print("device: " + device)
    with open(file_name, 'r') as f:
        for line in f.readlines():
            line = eval(line)
            for item in line[0]:
                if re.search(pattern, item):
                    device2 = item.split()[0].split(".")[0]
                    device_cdp_neighbors.append((device, device2))

# draw graph
my_graph = Digraph("My_Network")
my_graph.edge("s13", "Server")
my_graph.edge("s07", "MGMT_PC")
my_graph.edge("R1", "R2")
#my_graph.edge("R2", "R1")

for node in device_cdp_neighbors:
    node1, node2 = node
    my_graph.edge(node1, node2)

# fix positional mess
my_graph.render("outputs/cdp_neighbor_graph.gv")
source = my_graph.source
original_text = "digraph My_Network {"
new_text = 'digraph My_Network {\n{rank=same "R1" "R2"}\n{rank=same "s01" "s10"}\n{rank=same "s02" "s03" "s04" "s11" "s12" }\
    \n{rank=same s05 s06 s13}\n{rank=same s07 s08}\n{rank=same Server MGMT_PC}'
new_source = source.replace(original_text, new_text)
new_graph = Source(new_source)
new_graph.render("outputs/cdp_neighbor_graph_fixed.gv")

print(device_cdp_neighbors)