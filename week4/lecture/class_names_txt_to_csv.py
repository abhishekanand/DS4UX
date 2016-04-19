import csv
INPUT_FILE = "class_names_raw.txt"
OUTPUT_FILE = "class_names.csv"

name_list = []
with open(INPUT_FILE, "r") as ifile:
	reader = csv.reader(ifile, delimiter=',')
	for row in reader:
		row[0] = row[0].strip()
		row[1] = row[1].strip()
		name_list.append(row)

for i, n in enumerate(name_list, 1):
	n.insert(0,i)
	print(n)


with open(OUTPUT_FILE, "w") as output_file:
	writer=csv.writer(output_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_NONNUMERIC)
	writer.writerow(("num","name","favorite building"))
	for row in name_list:
#		print(row)
		writer.writerow(row)