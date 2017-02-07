import http.client
import json
from urllib.parse import quote_plus

def geo(address):
    connection=http.client.HTTPConnection("maps.google.com")
    # base = '/maps/api/geocode/json'
    # path = '{}?address={}'.format(base, quote_plus(address))
    base="/maps/api/geocode/json"
    path="{}?address={}".format(base,quote_plus(address))
    connection.request("GET",path)
    reply=connection.getresponse().read()
    reply1=json.loads(reply.decode("utf-8"))
    print(reply1)

geo("Ebad Al Rahman Mosque damitta")