$(document).ready(function(){
  $.ajax({

    // The 'type' property sets the HTTP method.
    // A value of 'PUT' or 'DELETE' will trigger a preflight request.
    type: 'GET',

    // The URL to make the request to.
    url: 'http://localhost:9898/tvshows',

    // The 'contentType' property sets the 'Content-Type' header.
    // The JQuery default for this property is
    // 'application/x-www-form-urlencoded; charset=UTF-8', which does not trigger
    // a preflight. If you set this value to anything other than
    // application/x-www-form-urlencoded, multipart/form-data, or text/plain,
    // you will trigger a preflight request.
    contentType: 'text/plain',

    xhrFields: {
      // The 'xhrFields' property sets additional fields on the XMLHttpRequest.
      // This can be used to set the 'withCredentials' property.
      // Set the value to 'true' if you'd like to pass cookies to the server.
      // If this is enabled, your server must respond with the header
      // 'Access-Control-Allow-Credentials: true'.
      withCredentials: false
    },

    headers: {
      // Set any custom headers here.
      // If you set any non-simple headers, your server must include these
      // headers in the 'Access-Control-Allow-Headers' response header.
    },

    success: function() {
      $.get('http://localhost:9898/tvshows', function( data ) {
        var obj = JSON.parse(data);
        var table = document.getElementById('show_table');
        for (var i = 0; i < obj.length; i++) {
          // Create a row and image.
          var row = table.insertRow(i);
          row.setAttribute('id', 'row_' + i)

          var img = document.createElement('img');
          var p = document.createElement('p');
          var buttonDetails = document.createElement('button');
          var buttonActors = document.createElement('button');
          var buttonSeasons = document.createElement('button');

          img.src = obj[i].poster;

          var cell_0 = row.insertCell(0);
          // var cell_1 = row.insertCell(1);

          buttonActors.setAttribute('class', 'details-actors btn btn-default btn-xs');
          buttonSeasons.setAttribute('class', 'details-seasons btn btn-default btn-xs');
          buttonDetails.setAttribute('id', 'actors-button');
          buttonActors.setAttribute('data-movie-id', obj[i].id);
          buttonSeasons.setAttribute('data-movie-id', obj[i].id);

          buttonDetails.setAttribute('class', 'details-button btn btn-default btn-xs');
          buttonDetails.setAttribute('data-movie-id', obj[i].id);

          buttonDetails.innerHTML = 'details';
          buttonActors.innerHTML = 'actors';
          buttonSeasons.innerHTML = 'seasons';

          cell_0.setAttribute('class', 'show-info');
          // cell_1.setAttribute('data-movie-details', 'none');
          // cell_1.setAttribute('id', obj[i].id);

          p.setAttribute('class', 'title');
          p.innerHTML = obj[i].name;
          cell_0.appendChild(buttonDetails);
          cell_0.appendChild(buttonActors);
          cell_0.appendChild(buttonSeasons);
          cell_0.appendChild(p);
          cell_0.appendChild(img);

        }

        // For every button in the table, add event handler.
        $('body').on('click','#show_table .details-button', function(e){
          row_data = this.dataset.movieId;
          $.get('http://localhost:9898/tvshow/' + this.dataset.movieId, function( data ) {
            var obj = JSON.parse(data);
            var overview = obj[0].overview;
            overview_p = document.getElementById('overview-content');
            data = $(overview_p).attr("data-movie-id");
            if (row_data === data) {
              overview_p.className += "visually-hidden";
              overview_p.setAttribute('data-movie-id', 0);
            } else {
              overview_p.className = "";
              overview_p.setAttribute('data-movie-id', row_data);
              overview_p.innerHTML = overview + "<h2>Network</h2>" + "<p>" + obj[0].network; "</p>";
            }
          })
        });


        $('body').on('click','#show_table .details-actors', function(e){
          row_data = this.dataset.movieId;
          $.get('http://localhost:9898/tvshow/' + this.dataset.movieId + '/actors', function( data ) {
            var obj = JSON.parse(data);
            var table = document.getElementById('details_table');
            data = $(table).attr("data-movie-details");
            if (data.movieDetails != 'actors') {
              table.innerHTML = "";
              for (var i = 0; i < obj.length; i++) {
                row = table.insertRow(i);
                var cell = row.insertCell(0);
                cell.innerHTML = obj[i].name;
              }
              table.setAttribute('data-movie-details', 'actors');
            }
          })
        });

        $('body').on('click','#show_table .details-seasons', function(e){
          row_data = this.dataset.movieId;
          $.get('http://localhost:9898/tvshow/' + this.dataset.movieId + '/seasons', function( data ) {
            var obj = JSON.parse(data);
            var table = document.getElementById('details_table');
            data = $(table).attr("data-movie-details");
            if (data.movieDetails != 'seasons') {
              table.innerHTML = "";
              for (var i = 0; i < obj.length; i++) {

                var buttonEpisodes = document.createElement('button');
                buttonEpisodes.setAttribute('class', 'details-episodes btn btn-default btn-xs');
                buttonEpisodes.setAttribute('data-season-id', obj[i].id);
                buttonEpisodes.setAttribute('data-movie-id', row_data);
                buttonEpisodes.innerHTML = 'episodes';

                row = table.insertRow(i);
                var cell = row.insertCell(0);
                cell.innerHTML = obj[i].number;
                cell.appendChild(buttonEpisodes);
              }
              table.setAttribute('data-movie-details', 'seasons');
            }
          });
        });

        $('body').on('click','#details_table .details-episodes', function(e){
          movieId = this.dataset.movieId;
          seasonId = this.dataset.seasonId;
          $.get('http://localhost:9898/tvshow/' + movieId + '/season/' + seasonId + '/episodes', function( data ) {
            var obj = JSON.parse(data);
            var table = document.getElementById('details_table');
            if (table.rows.length > obj.length) {
              for (var i = 0; i < obj.length; i++) {
                table.deleteRow(i + table.rows.length);
              }
            }
            for (var i = 0; i < obj.length; i++) {
              row = table.insertRow(table.length);
              var cell = row.insertCell(0);
              cell.innerHTML = obj[i].name;
            }
          });
        });
      });
    },

    error: function() {
      console.log('cors error');
      // Here's where you handle an error response.
      // Note that if the error was due to a CORS issue,
      // this function will still fire, but there won't be any additional
      // information about the error.
    }
    });
});
