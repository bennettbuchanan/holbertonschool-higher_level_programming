var https = require('https');

var options = {
    hostname: 'api.github.com',
    path: '/search/repositories?q=language:javascript&sort=stars&order=desc',
    headers: {
        'User-Agent': 'Holberton_School',
        'Authorization': 'token b8cb562142c180d22061d7f02543998b351cf649'
    }
};

var fs = require('fs');
fs.writeFile("/tmp/test", "[", function(err) {
    if (err) {
        return console.log(err);
    }
});

var printConsole = function (jsonString) {
    var obj = JSON.parse(jsonString);
    var array = [];
    for (i=0;i<30;i++){
        array.push(obj.items[i].full_name);
                        console.log(i);
    };

    function printThis(item) {

        // only store content before the slash
        var owner = item.substring(0, item.indexOf('/')); 

        var optionsOwner = {
            hostname: 'api.github.com',
            path: "/users/" + owner,
            headers: {
                'User-Agent': 'Holberton_School',
                'Authorization': 'token b8cb562142c180d22061d7f02543998b351cf649'
            }
        };

        var printOwner = function (jsonString) {
        var obj = JSON.parse(jsonString);

            var emptyJson = "{" + '"' + "full_name" + '"' + ":" + '"' + item + '"' + "," + '"' + "location" + '"' + ":" + '"' + obj.location + '"' + "}" + ",";
            fs.appendFile('/tmp/test', emptyJson, function (err) {
            });
        };

        var req = https.request(optionsOwner, function(res) {
            streamToString(res, printOwner);
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

    };

    array.map(printThis);
};

setTimeout(function(){ fs.appendFile('/tmp/test', "]", function (err) {
});}, 3000);

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