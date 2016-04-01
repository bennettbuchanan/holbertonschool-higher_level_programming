from urllib2 import Request, urlopen, URLError

target = open('/tmp/46', 'w')
target.truncate()
request = Request('https://api.github.com/search/repositories?q=language:python&sort=stars&order=desc')

try:
	response = urlopen(request)
	github_data = response.read()
	target.write(github_data)
        target.close()
        print "The file was saved!"
except URLError, e:
    print 'Error', e
