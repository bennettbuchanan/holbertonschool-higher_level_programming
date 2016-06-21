import urllib2, urllib

# The data to be sent, encoded.
data = urllib.urlencode([('id',46),('holdthedoor','submit')])

# Make the http request with the data as a header.
req = urllib2.Request('http://173.246.108.142/level0.php', data)
req.add_header("Content-type", "application/x-www-form-urlencoded")

# Open the URL with with the request 1024 times.
for i in range(0, 1024):
    urllib2.urlopen(req).read()
