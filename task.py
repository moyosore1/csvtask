import csv
import hashlib
import json


def convert_csv_to_json_file():
    open_csv_file = open("nft.csv")
    csvreader = csv.reader(open_csv_file)
    next(csvreader)
    dictionary_object = {}
    for index, row in enumerate(csvreader):
        dictionary_object[index] = {
            "Series_Number": row[1],
            "Filename": row[2],
            "Name": row[3],
            "Description": row[4],
            "Gender": row[5],
            "Attributes": row[6],
            "UUID": row[7],
        }
    open_csv_file.close()
    json_object = json.dumps(dictionary_object, indent=4)
    filename = f"converted_json_file.json"
    with open(filename, "w") as outfile:
        outfile.write(json_object)


def normalize_json(data: dict) -> dict:
    new_list = list()

    for key, value in data.items():
        new_data = dict()
        for k, v in value.items():
            new_data[k] = v
        new_list.append(new_data)
    return new_list


def outputfile():
    readable_hash = None
    with open("converted_json_file.json", "rb") as f:
        bytes = f.read()
        readable_hash = hashlib.sha256(bytes).hexdigest()
    if readable_hash:
        with open("converted_json_file.json", "r+") as file:
            file_data = json.load(file)
            for row in file_data.values():
                row["sha_256"] = readable_hash
            new_data = normalize_json(data=file_data)
            myFile = open("filename.output.csv", "w")
            writer = csv.writer(myFile)

            for index, dictionary in enumerate(new_data):
                if index == 0:
                    writer.writerow(dictionary.keys())
                writer.writerow(dictionary.values())
            myFile.close()


convert_csv_to_json_file()
outputfile()
