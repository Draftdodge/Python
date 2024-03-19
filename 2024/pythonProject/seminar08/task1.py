import json


def txt_to_json(source, output):
    data_new = {}
    with open(source, "r") as f:
        data = f.read()

    for line in data.split("\n"):
        name, number = line.split(" ")
        data_new[name.capitalize()] = float(number)

    with open(output, "w") as f_str:
        json.dump(data_new, f_str, indent=4)


txt_to_json("data.txt", "data.json")
