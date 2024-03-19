import pickle
import csv


def pickle_to_csv(pk_file, csv_file):
    with open(pk_file, "rb") as source:
        data = pickle.load(source)
    with open(csv_file, 'w', newline='') as out:
        writer = csv.DictWriter(out, fieldnames=data[0].keys())
        writer.writeheader()
        writer.writerows(data)


if __name__ == "__main__":
    pickle_to_csv("task4.pickle", "task6.csv")