
import http.client
import json
from urllib.parse import quote_plus

def geocode(address):
    base = '/maps/api/geocode/json'
    path = '{}?address={}'.format(base,quote_plus(address))
    connection = http.client.HTTPConnection('maps.google.com')
    connection.request('GET',path)
    reply = connection.getresponse().read()
    reply2 = json.loads(reply.decode('utf-8'))
    print(reply2['results'][0]['geometry']['location'])

if __name__=='__main__':
      address1 = '10 Downing St, London SW1A 2AB, UK'
      geocode(address1)