import requests
url = "http://127.0.0.1:8000/predict_get/" #BACKEND_URL 

data = {
    "VendorID": 1,
    "passenger_count": 1,
    "trip_distance": 2.1,
    "RatecodeID": 1,
    "store_and_fwd_flag": "N",
    "PULocationID": 142,
    "DOLocationID": 43,
    "payment_type": 2,
    "fare_amount": 8.0,
    "extra": 3.0,
    "mta_tax": 0.5,
    "tip_amount": 0,
    "tolls_amount": 0,
    "improvement_surcharge": 0.3,
    "total_amount": 11.8,
    "congestion_surcharge": 2.5,
    "airport_fee": 0
  }

import pickle
model = pickle.load(open("yellowcab/model/forest_model.pkl", "rb"))
l = []
for el in data.values():
    l.append(el)
print(list(l))
#data = [[VendorID, passenger_count, trip_distance, RatecodeID, store_and_fwd_flag, PULocationID, DOLocationID, payment_type, fare_amount,
        #extra, mta_tax, tip_amount, tolls_amount, improvement_surcharge, total_amount, congestion_surcharge, airport_fee]]
print(model.predict(list(l)))

url = "https://yellowcapapi-609285842864.europe-west9.run.app/" + "predict_get/"
response = requests.get(url, params = data) 
result = response.json()
print(result)