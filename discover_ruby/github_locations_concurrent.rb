extheaders = {
  'User-Agent' => 'Holberton_School',
  'Authorization' => 'token 6309c44b1fa175e71452a2b7e390792d807b08dc'
}

require 'lib/httpclient.rb'
http = HTTPClient.new
http.get "https://api.github.com/search/repositories?q=language:ruby&sort=stars&order=desc"
