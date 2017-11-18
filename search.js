$(window).load(function(){
    $('#search').keyup(function(){
        var searchField = $('#search').val();
        var regex = new RegExp(searchField, "i");
        var output = '<div class="row">';
        var count = 1;
        $.getJSON('data.json', function(data) {
          $.each(data, function(key, val){
            if ((val.name.search(regex) != -1) || (val.location.search(regex) != -1)) {
              output += '<div class="col-md-6 well">';
              output += '<div class="col-md-3"><img class="img-responsive" src="'+val.avatar+'" alt="'+ val.name +'" /></div>';
              output += '<div class="col-md-7">';
              output += '<h5>' + val.name + '</h5>';
              output += '<p>' + val.location + '</p>'
              output += '</div>';
              output += '</div>';
              if(count%2 == 0){
                output += '</div><div class="row">'
              }
              count++;
            }
          });
          output += '</div>';
          $('#results').html(output);
        }); 
    });
  });