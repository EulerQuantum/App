import csv
import requests
import json

key = "UZK46uo1msG53MNLgANhGi4PjSbvrnJi5HjG7qVp"
url = "https://api.data.gov/ed/collegescorecard/v1/schools.json?"

pages = [39,40,62,68,71,88,92,138,150,166,187,193,214,229,235,262,266,301,308,309,322,328]
counter = 0

for page in pages:
    
    names  = []
    urls   = []
    states = []
    
    counter+=1
    payload = {"api_key":key, "_page":page}

    
    try:
        
        response = requests.get(url, params = payload)
        
        response = json.loads(response.text)
        
        for i in range(20):
            
            try:
                names.append(response["results"][i]["school"]["name"])
                urls.append(response["results"][i]["school"]["school_url"])
                states.append(response["results"][i]["school"]["state"])
            except:
                continue
            
        with open("College4.csv","a") as File:
            fHand = csv.writer(File,delimiter=",")
            for n in range(len(names)):
                try:
                    fHand.writerow([names[n],urls[n],states[n]])
                except:
                    continue
        
                         
    except:
        print(page)
        
            





