$(document).ready(function() {
    $('.btn-back').on('click', function(event) {
        window.history.back();
    });

    $('.comment-reply-btn').on('click', function(event) {
        event.preventDefault();
        $(this).parent().parent('.row').parent('.container').parent('.media-body').parent('.media').next('.comment-reply').fadeToggle();
    });

    $('#avatar-picker').click(function(){
        $("#id_avatar").click();
    });
})