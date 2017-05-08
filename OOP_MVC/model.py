import csv

def get_data(csv_file):
    content=list()
    with open(csv_file) as fhand:
        reader=csv.reader(fhand, delimiter=",")
        for line in reader:
            content.append(tuple(line))
    return content


