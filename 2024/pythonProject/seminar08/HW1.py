import csv
import json
import os
import pickle


def get_dir_size(start_path='.'):
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(start_path):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            total_size += os.path.getsize(fp)
        for d in dirnames:
            dp = os.path.join(dirpath, d)
            total_size += get_dir_size(dp)
    return total_size


def save_result_to_json(results, file_name):
    with open(file_name, 'w', newline='') as f:
        json.dump(results, f, indent=4)


def save_result_to_csv(results, file_name):
    with open(file_name, 'w', newline='') as f:
        writer = csv.writer(f, dialect='excel')
        writer.writerow(['Path', 'Type', 'Size'])
        for i in results:
            writer.writerow([i['Path'], i['Type'], i['Size']])

def save_result_to_pickle(results, file_name):
    with open(file_name, 'wb') as f:
        pickle.dump(results, f)

def traverse_directory(directory) -> list:
    result = []
    for root, dirnames, filenames in os.walk(directory):
        for f in filenames:
            fp = os.path.join(root, f)
            file_size = os.path.getsize(fp)
            result.append({'Path': fp, 'Type': 'File', 'Size': file_size})
        for d in dirnames:
            dp = os.path.join(root, d)
            dir_size = get_dir_size(dp)
            result.append({'Path': dp, 'Type': 'Directory', 'Size': dir_size})
    return result


res = traverse_directory('C:\\Users\\Pavel\\Desktop\\study\\Python\\2024\\pythonProject\\seminar08\\')
save_result_to_json(res, 'hw1.json')
save_result_to_csv(res, 'hw1.csv')
save_result_to_pickle(res, 'hw1.pickle')
