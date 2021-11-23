import glob

for file in glob.glob("/tmp/logi_lldp/*"):
    device = file.split("/")[3].split("_")[0]
    print(device)