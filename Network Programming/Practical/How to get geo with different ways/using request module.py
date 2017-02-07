import requests

def geo(address):
    base="http://maps.googleapis.com/maps/api/geocode/json"
    paramters={"address":address}
    response=requests.get(base,params=paramters)
    results=response.json()
    print(results)

address1="Ebad Al Rahman Mosque damitta"
geo(address1)
