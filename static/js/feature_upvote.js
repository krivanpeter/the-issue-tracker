$('#like-button').on('click', function(event) {
    event.preventDefault();
    var quantity = 1;
    var likeCount = parseInt($('#number_of_upvotes').html());
	$.ajax({
		url: 'upvote',
		data: {
		    'quantity' : quantity
		},
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

$('#multiple-like-button').on('click', function(event) {
    event.preventDefault();
    var quantity = $(this).siblings('#quantity').val();
    var likeCount = parseInt($('#number_of_upvotes').html());
	$.ajax({
		url: 'upvote',
		data: {
		    'quantity' : quantity
		},
		dataType: 'JSON',
		success: function(data) {
            var newLikes;
            if(!data.max_reached){
                if (data.user_has_upvotes){
                    if (likeCount + data.quantity > 50){
                        data.quantity = 50 - likeCount;
                    }
                    likeCount += data.quantity;
                    $('#number_of_upvotes').html(likeCount);
                }
                else{
                    $('#missing_upvotes_error').fadeIn();
                }
            }
        }
    });
});