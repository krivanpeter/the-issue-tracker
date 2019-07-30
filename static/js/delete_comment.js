var csrftoken = getCookie('csrftoken');
var comment_id;
var actual_comment;

$('.comment-delete-btn').on('click', function(event){
    comment_id = $(this).siblings('.comment_id').val();
    $('#copied_comment').empty();
    actual_comment = $(this).parent('.col-3').parent('.row').parent('.container').parent('.media-body').parent('.media').clone();
    actual_comment.find('.comment-delete-btn').parent('.col-3').parent('.row').remove();
    actual_comment.find('.img-circle').addClass('thumbnail-img');
    actual_comment.find('.media-body').css('margin-left', '10px');
    $(actual_comment).appendTo($('#copied_comment'));
    $('#delCommModal').modal();
});

$('.delete_comment_form').on('submit', function(event) {
    console.log("ajax called");
    $.ajax({
        data: {
            'id': comment_id,
            csrftoken: csrftoken
        },
        type: 'POST',
        url: '/comment_delete/',
        success: function(data) {
            if (data.data = true) {
                console.log("delete")
            }
        }
    })
    event.preventDefault();
});