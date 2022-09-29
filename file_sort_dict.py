import os
import shutil

files = os.listdir('./data')

sorting_dict = {}
for file in files:
    if len(file.split('.')) > 1:
        ending = file.split('.')[-1]
        
        if ending in sorting_dict:
            sorting_dict[ending].append(file)
            continue
        sorting_dict[ending] = [file]
        
print(sorting_dict)

for dir in sorting_dict:
    for file in sorting_dict[dir]:
        shutil.move(f"./data/{file}",f"./data/{dir}/{file}")