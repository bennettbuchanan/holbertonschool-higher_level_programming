require 'httpclient'
require 'json'

extheaders = {
  'User-Agent' => 'Holberton_School',
  'Authorization' => 'token 6309c44b1fa175e71452a2b7e390792d807b08dc'
}

clnt = HTTPClient.new
url = 'https://api.github.com/search/repositories?q=language:ruby&sort=stars&order=desc'
response = clnt.get_content(url, nil, extheaders)
hash = JSON.parse(response)
items = hash["items"]
items.map {|e| puts e["full_name"]}
