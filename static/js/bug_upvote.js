$('#like-button').on('click', function(event) {
    event.preventDefault();
    var this_ = $(this).children('i');
    var likeCount = parseInt($('#number_of_likes').html());
	$.ajax({
		url: 'upvote',
		data: {},
		dataType: 'JSON',
		success: function(data) {
              var newLikes;
              if (data.user_upvoted){
                likeCount += 1;
                this_.html("Unlike");
                $('#number_of_likes').html(likeCount);
              } else {
                likeCount -= 1;
                this_.html("Like");
                $('#number_of_likes').html(likeCount);
          }}
    });
});