from posixpath import split
from graphviz import Digraph
import glob, re

pattern = re.compile("Eth [0123]/[0123]")

device_cdp_neighbors = []

for file_name in glob.glob("/home/maciej/repo/networking/ansible/cdp_example_output/*"):
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

print(device_cdp_neighbors)
