import requests
import matplotlib.pyplot as plt
#Get your own api key here https://developer.riotgames.com/
api_key = "ENTER OWN API KEY HERE"
username = input("Please enter a username: ")
accountdata = requests.get("https://euw1.api.riotgames.com/lol/summoner/v3/summoners/by-name/" + username + "?api_key=" + api_key)
summonerid = str(accountdata.json().get("id"))
championdata = requests.get("https://euw1.api.riotgames.com/lol/champion-mastery/v3/champion-masteries/by-summoner/" + summonerid + "?api_key=" + api_key)
chpointlist = []
for i in championdata.json():
    chpointlist.append(i["championPoints"])
plt.plot(chpointlist, "+")
plt.title("Champion points distribution of " + username)
plt.ylabel("Champion points")
plt.show()