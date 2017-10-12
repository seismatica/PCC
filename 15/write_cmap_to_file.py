import matplotlib.pyplot as plt
import json

cmap_list = [key for key in plt.cm.datad.keys() if not key.endswith("_r")]
cmap_list.sort()

with open("cmap_list.json", "w") as file_content:
    json.dump(cmap_list + [""], file_content)

cmap_text = ""
while cmap_list:
    cmap_line = []
    while len(cmap_line) < 8:
        cmap = cmap_list.pop(0)
        cmap_line.append(cmap)
    cmap_text += ", ".join(cmap_line) + "\n"

with open("cmap_text.txt", "w") as file_content:
    file_content.write(cmap_text)

