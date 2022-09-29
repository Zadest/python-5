import requests
from time import sleep
users = []

for i in range(10):
    sleep(0.2)
    response = requests.get('http://randomuser.me/api')
    if response.ok:
        user = response.json()
        print(user)
        users.append(user)

gender_count = {}

for user in users:
    if user['results'][0]['gender'] in gender_count:
        gender_count[user['results'][0]['gender']] += 1
        continue
    gender_count[user['results'][0]['gender']] = 1

print(users[0]['results'][0]['gender'])


male_list = [1 for user in users if user['results'][0]['gender'] == "male"]
male = sum(male_list)

female = sum([1 for user in users if user['results'][0]['gender'] == "female"])


min_age = min([user['results'][0]['dob']['age'] for user in users])
max_age = max([user['results'][0]['dob']['age'] for user in users])

print(min_age)
print(max_age)
print(f"{male=}, {female=}")