import yaml
import csv
import os
from random import shuffle

with open("config.yml", "r", encoding="utf-8") as f:
    config = yaml.safe_load(f)

OUTPUT_FOLDER = config["output_folder"]

files = [x for x in os.listdir(OUTPUT_FOLDER) if x != ".DS_Store"]
titles = []

# read the titles from each CSV in the `OUTPUT_FOLDER`
for file in files:
    with open(os.path.join(OUTPUT_FOLDER, file), "r", encoding="utf-8") as f:
        r = csv.DictReader(f)
        for row in r:
            titles.append(row["title"])

# shuffle the titles so there's no data leakage from channel
shuffle(titles)

# write the shuffled titles to a new file
with open("titles.csv", "w", encoding="utf-8") as f:
    w = csv.writer(f)
    w.writerow(["title"])
    for title in titles:
        w.writerow([title])
        
# write the titles from the csv to a txt file (ReidDotO change)
with open('titles.csv', 'r') as inp, open('titles.txt', 'w') as out:
    for line in inp:
        out.write(line)