from urllib2 import Request, urlopen, URLError
import requests
from requests_oauthlib import OAuth1
import json

i = 0
url = 'https://api.github.com/user'
auth = OAuth1('token 6309c44b1fa175e71452a2b7e390792d807b08dc', 'Holberton_School')
request = requests.get(url, auth=auth)


try:
	response = urlopen(request)
	github_data = response.read()
except URLError, e:
    print 'Error', e

json_data = json.loads(github_data)
for number in json_data['items']:
	try:
		response = urlopen(json_data['items'][i]['owner']['url'])
		data = response.read()
		location_data = json.loads(data)
		print '{"location": "%s"}' % location_data['location']
	except URLError, e:
	    print 'Error', e
	i += 1
