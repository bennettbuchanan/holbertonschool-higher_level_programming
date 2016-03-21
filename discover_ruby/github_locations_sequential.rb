require 'httpclient'
require 'json'
require 'thread'

extheaders = {
  'User-Agent' => 'Holberton_School',
  'Authorization' => 'token 6309c44b1fa175e71452a2b7e390792d807b08dc'
}

clnt = HTTPClient.new
url = 'https://api.github.com/search/repositories?q=language:ruby&sort=stars&order=desc'
response = clnt.get_content(url, nil, extheaders)
hash = JSON.parse(response)
items = hash["items"]

full_name = items.map do |e|
  owner = e["owner"]
  owner_url = owner["url"]
  owner_response = clnt.get_content(owner_url, nil, extheaders)
  owner_hash = JSON.parse(owner_response)
  {full_name: e["full_name"], location: owner_hash["location"]}
end

puts full_name.to_json
