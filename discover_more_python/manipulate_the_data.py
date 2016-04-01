from urllib2 import Request, urlopen, URLError
import json

i = 0
request_headers = {
  'User-Agent': 'Holberton_School',
  'Authorization': 'token 6309c44b1fa175e71452a2b7e390792d807b08dc'
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
    print json_data['items'][i]['full_name']
    i += 1
