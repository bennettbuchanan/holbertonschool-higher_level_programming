from multiprocessing import Process, Pool
import urllib2
from urllib2 import Request, urlopen, URLError
import json

i = 0
array= []
items = []

request_headers = {
  'User-Agent': 'Holberton_School',
  'Authorization': 'token 8cf3d6e86105e4fa1f9af922bcee9ae0db3d1149'
}

url = 'https://api.github.com/search/repositories?q=language:python&sort=stars&order=desc'
request = Request(url, None, request_headers)

try:
	response = urlopen(request)
	github_data = response.read()
except URLError, e:
    print 'Error', e

json_data = json.loads(github_data)
for number in json_data['items']:
	try:
		items.append(json_data['items'][i])
	except URLError, e:
	    print 'Error', e
	i += 1

def http_get(url):
    get_data = url['owner']['url']
    full_name = url['full_name']
    request = Request(get_data, None, request_headers)
    response = urllib2.urlopen(request, timeout=5).read()
    location_data = json.loads(response)
    return {'location': location_data['location'], 'full_name': url['full_name']}

pool = Pool(processes=5)
results = pool.map(http_get, items)

for result in results:
    array.append(result)

name_and_location = json.dumps(array, sort_keys=True)
print name_and_location
