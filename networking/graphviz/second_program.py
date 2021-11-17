import glob, re
from graphviz import Digraph, Source

pattern = re.compile('eth1/[0123]')

device_lldp_neighbors = []

