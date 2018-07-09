import requests
import Segment


#segment idsini alıyor. Fonksiyona parametre olarak veriyor.
def getInput():
    segArr = Segment.listSegments()
    inp = int(input("\n Lider Tablosunu Görmek İstediğiniz Segmenti Seçiniz: "))
    print("\n", segArr[inp].name , " Lider Tablosu")
    atheleteArr = getBoard(str(segArr[inp].id), segArr[inp].distance)
    athName = input(" \n Atlet ismi giriniz: ")
    print("\n Bu tabloda ", counterAthelete(athName,atheleteArr), " kez var.")


class Athelete:
    def __init__(self, name, time, rank):
        self.name = name
        self.time = time
        self.rank = rank
    def setSkor(self, skor):
        self.skor = skor

def getBoard(id, distance):
    segmentid=id
    endpoint='https://www.strava.com/api/v3/segments/'+segmentid+'/leaderboard?page=1&per_page=50&'
    #endpoint='https://www.strava.com/api/v3/segment_efforts/7171356&'
    headers = {'access_token': 'db66b2e6abe30e7c645135c232f3fa4da78d5350'}
    #Stravaya üye olunurken alınan API key


    r = requests.get(endpoint, json=headers)
    #print(r.json())
        #print('Segment ID: {}'.format(r.json()["segments"][0]["id"]))
        # print('Segment Adı: {}'.format(r.json()["segments"][0]["name"]))
    atheleteArr = []
    for item in r.json()["entries"]: # print(item["name"])
        a = Athelete(item["athlete_name"], item["elapsed_time"], item["rank"])
        a.setSkor(calculateSkor(a, distance))
        atheleteArr.append(a)
        print('Atlet Adı: {}'.format(item["athlete_name"]), ' - Bitirme Zamanı: {}'.format(item["elapsed_time"]),
               ' - Derecesi: {}'.format(item["rank"]), " - Skor:", a.skor)
    return atheleteArr

#Skor hesabı yapar
def calculateSkor(athelete, distance):
    skor = int(9**(distance / athelete.time)/10000000)
    return skor


# Seçilen Atletin o segmentte leaderboardta kaç kere listelendiğini sayar.
def counterAthelete(name, atheleteArr):
    sayac = 0
    for item in atheleteArr:
       if(item.name == name):
            sayac = sayac + 1
    return sayac


