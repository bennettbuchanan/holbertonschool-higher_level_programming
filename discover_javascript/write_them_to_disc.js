var https = require('https');

var options = {
    hostname: 'api.github.com',
    path: '/search/repositories?q=language:javascript&sort=stars&order=desc',
    headers: {
        'User-Agent': 'Holberton_School',
        'Authorization': 'token b8cb562142c180d22061d7f02543998b351cf649'
    }
};

var printConsole = function (jsonString) {
    var fs = require('fs');
    fs.writeFile("/tmp/46", jsonString, function(err) {
        if (err) {
            return console.log(err);
        }
           console.log("The file was saved!");
    });
};

var req = https.request(options, function(res) {
    streamToString(res, printConsole) ;
});

req.end(); 

function streamToString(stream, cb) {
    const chunks = [];
    stream.on('data', (chunk) => {
        chunks.push(chunk);
    });
    stream.on('end', () => {
        cb(chunks.join('')); 
    });
};

req.on('error', function(e) {
    console.error(e);   
});