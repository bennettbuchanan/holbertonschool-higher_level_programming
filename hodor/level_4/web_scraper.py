from lxml import html
import requests

page = requests.get('http://econpy.pythonanywhere.com/ex/001.html')
tree = html.fromstring(page.content)

fields = tree.xpath('//div[@title="buyer-name"]/text()')

print 'fields: ', fields
