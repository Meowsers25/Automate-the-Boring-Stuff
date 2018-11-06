import requests

res = requests.get('https://automatetheboringstuff.com/files/rj.txt')
print(type(res))
# print(res.status_code == requests.codes.ok)
# always call raise_for_status after calling requests.get
print(res.raise_for_status())
play_file = open('RomeoAndJuliet.txt', 'wb')
for chunk in res.iter_content(100000):
    print(play_file.write(chunk))
play_file.close()
# print(len(res.text))
# print(res.text[:250])