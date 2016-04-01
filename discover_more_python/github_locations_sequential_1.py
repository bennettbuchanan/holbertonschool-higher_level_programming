from urllib2 import Request, urlopen, URLError
import json

i = 0
array= []
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
		request2 = Request(json_data['items'][i]['owner']['url'], None, request_headers)
		response = urlopen(request2)
		data = response.read()
		location_data = json.loads(data)
		array.append({'location': location_data['location'], 'full_name': json_data['items'][i]['full_name']})
		final = json.dumps(array)
	except URLError, e:
	    print 'Error', e
	i += 1

print final
