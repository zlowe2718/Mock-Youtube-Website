$(document).ready(function() {
  $('.likein').click(function(){
    $.ajax({
            type: "POST",
            data: {'content': "video-like",'operation':'like_submit','csrfmiddlewaretoken': window.CSRF_TOKEN},
            dataType: "json",
            success: function(response) {
              selector = $('.like-img');
                    var like_count = $('#like-counter').text();
                    if(response.liked==true){
                      //maybe have a response url from django here instead?
                      $(selector).attr('src',  '/static/icons/blue-like-button.png');
                      $('#like-counter').text(parseInt(like_count) + 1);
                    }
                    else if(response.liked==false){
                      $(selector).attr('src', '/static/icons/youtube-like-button-png-11.png')
                      $('#like-counter').text(parseInt(like_count) - 1);
                    }
              }
        });
  });
});