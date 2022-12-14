from collections import defaultdict
import os
import shutil

file = open("C:\\Users\\DSouzaJ\\Desktop\\Datasets\\nfdi4ds-leaderboard-extraction-shared-task\\resultsAnnotation.tsv", encoding="utf8")
parent_dir = "C:\\Users\\DSouzaJ\\Desktop\\Datasets\\nfdi4ds-leaderboard-extraction-shared-task\\new-annotated-data"
src = "C:\\Users\\DSouzaJ\\Desktop\\Datasets\\nfdi4ds-leaderboard-extraction-shared-task\\pdfFile_xml"

check = "C:\\Users\\DSouzaJ\\Desktop\\Datasets\\nfdi4ds-leaderboard-extraction-shared-task\\old_pdfFile_xml"

Lines = file.readlines()

counter = 0

for line in Lines:

    line = line.strip()

    tokens = line.split("\t")

    if len(tokens) != 2:
        continue

    filename = tokens[0].replace(".pdf", ".tei.xml")
    annotations = tokens[1].split("$")

    path = os.path.join(parent_dir, str(counter))
    src_path = os.path.join(src, filename)

    check_path = os.path.join(check, filename)

    if os.path.isfile(check_path):
        continue

    if not os.path.isfile(src_path):
        continue

    if not os.path.isdir(path):
        os.mkdir(path)

    anno_f = open(path+"\\annotations.txt","w+", encoding="utf-8")
    for annotation in annotations:
        anno_f.write(annotation+"\n")
    anno_f.close()    

    dst_path = os.path.join(path, filename)
    shutil.copy(src_path, dst_path)    

    print(filename)

    counter = counter+1
