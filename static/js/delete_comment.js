var csrftoken = getCookie('csrftoken');
var comment_id;
var actual_comment;


$('.children-comment-delete-btn').on('click', function(event){
    comment_id = $(this).siblings('.comment_id').val();
    $('#copied_comment').empty();
    actual_comment = $(this).parent().parent('.media-body').parent('.media').clone();
    actual_comment.find('.children-comment-delete-btn').parent('div').remove();
    actual_comment.find('.img-circle').addClass('thumbnail-img');
    actual_comment.find('.media-body').css('margin-left', '10px');
    $(actual_comment).appendTo($('#copied_comment'));
    $('#delCommModal').modal();
});

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
    $.ajax({
        data: {
            'id': comment_id,
            csrftoken: csrftoken
        },
        type: 'POST',
        url: '/comment-delete/',
        success: function(data) {
            if (data.data = true) {
                $('#delCommModal').modal('hide');
                location.reload();
            }
        }
    })
    event.preventDefault();
});