import json
import requests
import csv


#Define the basic Url and the api_key
url = "https://api.data.gov/ed/collegescorecard/v1/schools.json?"
key = "UZK46uo1msG53MNLgANhGi4PjSbvrnJi5HjG7qVp"

counter = 1

#Makes a get request for all the pages in the api(358 pages showing 20 insitutions per page)
for i in range(358):
        
    payload = {"_page": i, "api_key": key}
    names  = []
    urls   = []
    states = []


    try:
            
        response = requests.get(url, params=payload)
        response = json.loads(response.text)

        #Saves the name,url, and state of each institution
        with open("College.csv","a") as File:
            
            fHand = csv.writer(File,delimiter=",")
                
            for i in range(20):
                #Get the data for each of the 20 instituitions per page
                names.append(response["results"][i]["school"]["name"])
                urls.append(response["results"][i]["school"]["school_url"])
                states.append(response["results"][i]["school"]["state"])

            for i in range(len(names)):
                fHand.writerow([names[i],urls[i],states[i]])
                print(names[i],",",urls[i],",",states[i])
                


            counter+=1
                
               

    except:
        
        with open("Logger.txt","a") as File:

            #Logs to a different file the page that failed to load and skips to the next one
            File.write("poblem caused the program to skip at the ")
            File.write(str(counter+1))
            File.write(" page")
            File.write("\n")
            continue



            
