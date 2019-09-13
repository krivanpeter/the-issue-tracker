$("#quantity").on('keyup', function (e) {
    if (e.keyCode === 13) {
        $('#upvote-button').click();
    }
});

$('#upvote-button').on('click', function(event) {
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
            else{
                location.reload();
            }
        }
    });
});