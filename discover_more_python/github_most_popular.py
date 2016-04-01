from urllib2 import Request, urlopen, URLError

request = Request('https://api.github.com/search/repositories?q=language:python&sort=stars&order=desc')

try:
	response = urlopen(request)
	github_data = response.read()
	print github_data
except URLError, e:
    print 'Error', e
