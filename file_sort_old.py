import os
import shutil

path = "./data"

files = os.listdir(path=path)

sortingDictionary = {}

for file in files:
    file_ending = file.split('.')[-1]

    if len(file.split('.')) == 1:
        continue

    if file_ending in sortingDictionary:
        sortingDictionary[file_ending].append(file)
    else:
        sortingDictionary[file_ending] = [file]

print(sortingDictionary)

for folder in sortingDictionary:
    print(folder)
    for filename in sortingDictionary[folder]:
        shutil.move(f"{path}/{filename}",f"{path}/{folder}/{filename}")
        print(f"{path}/{filename}",' ---> ',f"{path}/{folder}/{filename}")
