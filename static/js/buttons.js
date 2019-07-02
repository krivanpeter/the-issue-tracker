$(document).ready(function() {
    $('.btn-back').on('click', function(event) {
        window.history.back();
    });

    $('.comment-reply-btn').on('click', function(event) {
        event.preventDefault();
        $(this).parent().parent().next('.comment-reply').fadeToggle();
    });
})