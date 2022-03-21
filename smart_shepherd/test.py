from typing import List
import requests

def animal_notification_parser(payload: dict) -> List[float]:

   list = payload["data"]
   id = list[0]["id"]
   location = list[0]["location"]["value"]
   coordinates = location["coordinates"]

   return id,coordinates

DATA = {
   "id":"urn:ngsi-ld:Notification:622a2d33ae80219981811480",
   "type":"Notification",
   "subscriptionId":"urn:ngsi-ld:Subscription:622a213c586ba435bc38011e",
   "notifiedAt":"2022-03-10T16:54:11.490Z",
   "data":[
      {
         "id":"urn:ngsi-ld:Animal:0001",
         "type":"Animal",
         "location":{
            "type":"GeoProperty",
            "value":{
               "type":"Point",
               "coordinates":[
                  4.165,
                  5.6133,
                  -1.1292
               ]
            }
         },
         "species":{
            "type":"Property",
            "value":"cow"
         },
         "animalActivity":{
            "type":"Property",
            "value":"Stand up"
         }
      }
   ]
}

X = animal_notification_parser(DATA)
print(X)


def temperature_parser():
   # gets temperature data and parses it

   orion = "localhost:1026"
   sensor_id = "001"
   url = f"http://{orion}/ngsi-ld/v1/entities/urn:ngsi-ld:TemperatureSensor:{sensor_id}"
   headers = {"Content-Type": "application/json"}

   try:
      response = requests.request("GET", url, headers=headers)
   except requests.HTTPError as e:
      if e.response.status_code == 404:
         return e

   temperature = response.json()
   temperature = temperature["temperature"]["value"]

   return temperature


#x = temperature_parser()
#print(x)