from urllib2 import Request, urlopen, URLError
import json

i = 0
request = Request('https://api.github.com/search/repositories?q=language:python&sort=stars&order=desc')

try:
	response = urlopen(request)
	github_data = response.read()
except URLError, e:
    print 'Error', e

json_data = json.loads(github_data)
for number in json_data['items']:
    print json_data['items'][i]['full_name']
    i += 1
