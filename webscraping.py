import requests
import sys
import json
from bs4 import BeautifulSoup

lst = []

for i in range(1):
    r = requests.get("https://filmtube.live/films.html?page=" + str(i + 1)) 
    data = r.content

    soup = BeautifulSoup(data, "html.parser")

    #we take the tag <figure>
    for figure in soup.find_all('figure'): 
        html = figure
        soup = html
        dataList = []

        # Titles from movies 
        for a in soup.find_all('a'): #We take tag <a>
            html = a
            soup = html

            req = requests.get("https://filmtube.live/" + a.get("href")) 
            linkHtml = req.content
        

            finalLinkGetter = BeautifulSoup(linkHtml, "html.parser")
            iframe = finalLinkGetter.find(id="player")
            dataList.append("https://filmtube.live/" + iframe.get("src"))

            # Images / Names
            for img in soup.find_all('img'): #We take tag <img> to gather the images
                dataList.append(img.get("data-src"))
                dataList.append(img.get("alt"))
                lst.append(dataList)


# films.json = final file
with open('films.json', 'wt', encoding="utf-8") as outfile: #Create or open the final file
    for list in lst:
        filmJson = {"nom": list[2], "lien": list[0], "cover": list[1]} 
        json.dump(filmJson, outfile) #Write the file on each iteration
        outfile.write("\n") # retour à la ligne pour chaque film 
        

    

