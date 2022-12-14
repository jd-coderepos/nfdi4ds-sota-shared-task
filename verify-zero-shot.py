import os
import shutil

file = open("C:\\Users\\DSouzaJ\\Desktop\\Datasets\\nfdi4ds-sota-shared-task\\df_zero_shot.tsv", encoding="utf8")
Lines = file.readlines()
files_dict = {}

for line in Lines:
    line = line.strip()
    line = line.replace(".pdf", ".tei.xml")
    files_dict[line] = 0

dir = "C:\\Users\\DSouzaJ\\Desktop\\Datasets\\nfdi4ds-sota-shared-task\\new-annotated-data"
dst = "C:\\Users\\DSouzaJ\\Desktop\\Datasets\\nfdi4ds-sota-shared-task\\zero-shot-data"
file_out = open("C:\\Users\\DSouzaJ\\Desktop\\Datasets\\nfdi4ds-sota-shared-task\\not_present.txt","w+", encoding="utf-8")
file_out_new =  open("C:\\Users\\DSouzaJ\\Desktop\\Datasets\\nfdi4ds-sota-shared-task\\new_dump.txt","w+", encoding="utf-8")

counter = 0
for folder in os.listdir(dir):

    data_dir = os.path.join(dir, folder)

    for file in os.listdir(data_dir):

        if "tei.xml" in file:
            file_out_new.write(file+"\n")

            if file not in files_dict.keys():
                file_out.write(file+"\n")
                continue
            src_path = os.path.join(data_dir, file)
            dst_data_path = os.path.join(dst, str(counter))

            if not os.path.isdir(dst_data_path):
                os.mkdir(dst_data_path)

            dst_path = os.path.join(dst_data_path, file)
            shutil.copy(src_path, dst_path)

            src_anno_path = os.path.join(data_dir, "annotations.txt")
            dst_anno_path = os.path.join(dst_data_path, "annotations.txt")
            shutil.copy(src_anno_path, dst_anno_path)

            counter = counter+1
