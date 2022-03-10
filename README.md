# AI PoC for real-time animal activity recognition

## Introduction
The aim of this PoC is to allow an AI service provider to offer it’s service on a public marketplace, where a service consuming party can acquire access to this offer, inject input data into it and receive predictions resulting from the inference with a trained AI model.

The AI service is providing real-time prediction and by means of having a Context Broker deployed in the offered service, the data provisioning will be in real-time from the data source(s) to the AI model and respectively publishing the results of the predictions to the consumer application via a Context Broker on the consumer side. 

## Architecure
This PoC implements the following architecture: 

![architecture](https://github.com/RihabFekii/ai-poc/blob/dev/doc/Architecture%20diagrams-Usage%20of%20AI%20service.jpg)

For a better understanding of the PoC, the above architecture could be devided to 3 main steps as folllows:

* **Step 1:**  Smart Shepehrd Inc. subscribes to the Context Broker of Happy Cattle Co. to receive in an automated way animal coordinates update in its Context Broker by means of a Notification Proxy 

* **Step 2:** The AI service sends HTTP Requests to retrieve animal data from its own Context Broker and to retrieve temerature data from the Context Broker of Real Time Weather

* **Step 3:** Happy Cattle Co. subscribes to receive predictions updates from the Context Broker of Smart Shepherd Inc. by means of a Notification Proxy 


## Step 1:

* Run the docker-compose file in smart-shepherd folder: 
```shell 
cd smart-shepherd
docker-compose up
 ```

* Run the docker-compose file in happy-cattle folder: 
```shell 
cd happy-cattle
docker-compose up
 ```

First, start with creating a subsciption from the Context Broker of Smart Shepherd to the Context Broker of Happy Cattle. This will enable Smart Shepherd to receive notification of animal coordinates update. 

* Smart Shepherd creates a subscription:
```shell
   curl -v --location --request POST 'localhost:1029/ngsi-ld/v1/subscriptions/' \
      --header 'Content-Type: application/json' \
      --data-raw ' {
         "description":"Notify me of new animal coordinates",
         "type":"Subscription",
         "name":"animalCoordinatesSubscription",
         "entities":[
            {
               "type":"Animal"
            }
         ],
         "notification":{
            "endpoint":{
               "uri":"http://ai.notification-proxy.docker:8080/notification",
               "accept":"application/json"
            }
         }
      }'
  ```
* Create an entity at the Contect Broker of Happy Cattle:
```shell
   curl -v --location --request POST 'localhost:1029/ngsi-ld/v1/entities' \
      --header 'Content-Type: application/json' \
      --data-raw '{
         "id":"urn:ngsi-ld:Animal:0001",
         "type":"Animal",
         "species":{
            "type":"Property",
            "value":"cow"
         },
         "location":{
            "type":"GeoProperty",
            "value":{
               "type":"Point",
               "coordinates":[
                  3.165,
                  2.6133,
                  -1.4292
               ]
            }
         }
      }'
```
* Query Smart Shephered Broker: 
```shell
   curl --location --request GET 'localhost:1028/ngsi-ld/v1/entities/urn:ngsi-ld:Animal:0001'
``` 

Here you should have as a result an entity of Type animal created in the Context Broker of Smart Shepherd

* Update a property in the Context Broker of Happy Cattle: 
```shell
   curl -v --location --request POST 'localhost:1029/ngsi-ld/v1/entities/urn:ngsi-ld:Animal:0001/attrs' \
      --header 'Content-Type: application/json' \
      --data-raw '{
         "location":{
            "type":"GeoProperty",
            "value":{
               "type":"Point",
               "coordinates":[
                  4.165,
                  3.6133,
                  -1.1292
               ]
            }
         }
      }'
```
* Query the Broker of Smart Shepehrd:
 ```shell
   curl --location --request GET 'localhost:1028/ngsi-ld/v1/entities/urn:ngsi-ld:Animal:0001'
 ``` 
 
## Step 2 

* Run the docker-compose file in real_time_weather folder: 

```shell 
cd real_time_weather
docker-compose up 
````

First, create a TemperatureSensor entity at the Context Broker of Real Time Weather: 

```shell
   curl -v --location --request POST 'localhost:1026/ngsi-ld/v1/entities' \
      --header 'Content-Type: application/json' \
      --data-raw '{
         "id":"urn:ngsi-ld:TemperatureSensor:001",
         "type":"TemperatureSensor",
         "dateObserved":{
            "type":"Property",
            "value":"2016-11-30T07:00:00.00Z"
         },
         "temperature":{
            "type":"Property",
            "value":17
         }
      }'
```

* To check that this entity is created, query the Context Broker of Real Time Weather:
 ```shell
   curl --location --request GET 'localhost:1026/ngsi-ld/v1/entities/urn:ngsi-ld:TemperatureSensor:001'
 ```


## Step 3: 

This last step will ensure that at the moment when the prediction of the animal activity is calculated by the AI service, the prediction attribute at the Context Broker of Happy Cattle will be created/updated. This is possible by means of subscribing to the Context Broker of Smart Shepeherd to receive notification of prediction update.

- First, Happy Cattle creates a subscription at the Context Broker of Smart Shepherd: 

```shell
   curl -v --location --request POST 'localhost:1028/ngsi-ld/v1/subscriptions/' \
      --header 'Content-Type: application/json' \
      --data-raw ' {
         "description":"Notify me of new animal activity prediction",
         "type":"Subscription",
         "name":"predictionSubscription",
         "entities":[
            {
               "type":"Animal"
            }
         ],
         "notification":{
            "endpoint":{
               "uri":"http://farm.notification-proxy.docker:8081/notification",
               "accept":"application/json"
            }
         }
      }'
  ```

- Run the following command to calculate prediction:

````shell
cd smart_shepherd/ 
python main.py
````

- Then query the Context Broker of Happy Cattle:

```shell
   curl --location --request GET 'localhost:1029/ngsi-ld/v1/entities/urn:ngsi-ld:Animal:0001'
```

