import requests

#API url adresimiz
endpoint = 'https://www.strava.com/api/v3/segments/explore?bounds=40.85260833969849,28.645335828710927,41.163500149058684,29.31138197128905&activity_type=riding&min_cat=0&max_cat=0&'

#Stravaya üye olunurken alınan API key
headers = {'access_token': 'db66b2e6abe30e7c645135c232f3fa4da78d5350'}


r = requests.get(endpoint, json=headers)
# print(r.json())

class Segment:
    def __init__(self, id, name, distance):
        self.id = id
        self.name = name
        self.distance = distance

# Stravdan segmentleri çekiyor,yazdırıyor ve obje olarak döndürüyor
def listSegments():
    counter = 0
    segArr = []
    for item in r.json()["segments"]: # print(item["name"])
        s = Segment(item["id"], item["name"], item["distance"])
        segArr.append(s)
        print(str(counter) + '.) Segment ID: {}'.format(item["id"]), ' - Segment Adı: {}'.format(item["name"]),
                  ' - Distance: {}'.format(item["distance"]))
        counter = counter + 1
    return segArr



