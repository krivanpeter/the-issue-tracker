$('#like-button').on('click', function(event) {
    event.preventDefault();
    var this_ = $(this).children('i');
    var likeCount = parseInt($('#number_of_upvotes').html());
	$.ajax({
		url: 'upvote',
		data: {},
		dataType: 'JSON',
		success: function(data) {
              var newLikes;
              if (data.feature_upvoted){
                likeCount += 1;
                this_.html(" Upvote Again");
                $('#number_of_upvotes').html(likeCount);
              }
          }
    });
});