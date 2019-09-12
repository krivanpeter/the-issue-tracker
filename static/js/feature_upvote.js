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
            if(!data.max_reached){
                if (data.user_has_upvotes){
                    likeCount += 1;
                    $('#number_of_upvotes').html(likeCount);
                }
                else{
                    $('#missing_upvotes_error').fadeIn();
                }
            }
        }
    });
});