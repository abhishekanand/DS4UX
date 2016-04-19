INPUT_FILE = "class_names_raw.txt"
OUTPUT_FILE = "class_names.tsv"

name_list = []
with open(INPUT_FILE, "r") as ifile:
    for n in ifile.readlines():
        n = n.strip().split(",")
        for i,x in enumerate(n):
            n[i] = n[i].strip(" \t")
        name_list.append(n)
        print(n)

with open(OUTPUT_FILE, "w") as ofile:
    for i, n in enumerate(name_list, 1):
        ofile.write(str(i) + "\t" + n[0] + "\t" + n[1] + "\n")
