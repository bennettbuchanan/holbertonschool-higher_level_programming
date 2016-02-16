var https = require('https');

var options = {
    hostname: 'api.github.com',
    path: '/search/repositories?q=language:javascript&sort=stars&order=desc',
    headers: {
        'User-Agent': 'Holberton_School',
        'Authorization': 'token b8cb562142c180d22061d7f02543998b351cf649'
    }
};

var req = https.request(options, function(res) {
    res.on('data', function(d) {
    process.stdout.write(d);
  });
});

req.end();

req.on('error', function(e) {
  console.error(e);
});