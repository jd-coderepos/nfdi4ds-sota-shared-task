import os
import shutil

dir = "C:\\Users\\DSouzaJ\\Desktop\\Datasets\\nfdi4ds-sota-shared-task\\annotated-data"
annotations = {}
for folder in os.listdir(dir):
    data_dir = os.path.join(dir, folder)
    anno_file = open(os.path.join(data_dir, "annotations.txt"), encoding="utf8")
    Lines = anno_file.readlines()
    for line in Lines:
        line = line.strip()
        tokens = line.split("#")
        annotation = tokens[0]+"#"+tokens[1]+"#"+tokens[2]
        if annotation in annotations.keys():
            count = annotations[annotation]
            count = count+1
            annotations[annotation] = count
        else:
            annotations[annotation] = 1

#sorted_annotations = dict(sorted(annotations.items(), key=lambda item: item[1], reverse=True))

#count = 0

#for anno in sorted_annotations.keys():
#    print(anno+"\t"+sorted_annotations[anno])

#if at least one of annotations is not in the global annotations list, move the file to zero shot

counter_annotated_data = 5531
counter = 0

zero_shot_dir = "C:\\Users\\DSouzaJ\\Desktop\\Datasets\\nfdi4ds-sota-shared-task\\zero-shot-data"
dir = "C:\\Users\\DSouzaJ\\Desktop\\Datasets\\nfdi4ds-sota-shared-task\\new-annotated-data"
anno_dir = "C:\\Users\\DSouzaJ\\Desktop\\Datasets\\nfdi4ds-sota-shared-task\\add-to-annotated-data"

file_out_zero_shot = open("C:\\Users\\DSouzaJ\\Desktop\\Datasets\\nfdi4ds-sota-shared-task\\zero-shot-files.txt","w+", encoding="utf-8")

for folder in os.listdir(dir):
    data_dir = os.path.join(dir, folder)
    anno_file = open(os.path.join(data_dir, "annotations.txt"), encoding="utf8")
    Lines = anno_file.readlines()
    annotation_found = True
    for line in Lines:
        line = line.strip()
        tokens = line.split("#")
        annotation = tokens[0]+"#"+tokens[1]+"#"+tokens[2]
        if annotation not in annotations.keys():
            annotation_found = False
            #move file to zero shot
            for file in os.listdir(data_dir):
                if "tei.xml" not in file:
                    continue
                
                file_out_zero_shot.write(file+"\n")

                dst_data_path = os.path.join(zero_shot_dir, str(counter))

                if not os.path.isdir(dst_data_path):
                    os.mkdir(dst_data_path)                

                src_path = os.path.join(data_dir, file)
                dst_path = os.path.join(dst_data_path, file)
                shutil.copy(src_path, dst_path)

                src_path = os.path.join(data_dir, "annotations.txt")
                dst_path = os.path.join(dst_data_path, "annotations.txt")
                shutil.copy(src_path, dst_path)

                counter = counter+1
            break
    if annotation_found:
        #move file to add to annotated data
        for file in os.listdir(data_dir):

            if "tei.xml" not in file:
                continue

            dst_data_path = os.path.join(anno_dir, str(counter_annotated_data))  

            if not os.path.isdir(dst_data_path):
                os.mkdir(dst_data_path)                

            src_path = os.path.join(data_dir, file)
            dst_path = os.path.join(dst_data_path, file)
            shutil.copy(src_path, dst_path)

            src_path = os.path.join(data_dir, "annotations.txt")
            dst_path = os.path.join(dst_data_path, "annotations.txt")
            shutil.copy(src_path, dst_path)

            counter_annotated_data = counter_annotated_data+1                 





