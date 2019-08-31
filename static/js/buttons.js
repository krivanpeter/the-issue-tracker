$(document).ready(function() {
    $('.btn-back').on('click', function(event) {
        window.history.go(-1);
    });

    $('.comment-reply-btn').on('click', function(event) {
        event.preventDefault();
        $(this).parent().parent('.row').parent('.container').parent('.media-body').parent('.media').next('.comment-reply').fadeToggle();
    });

    $('#avatar-picker').click(function(){
        $("#id_avatar").click();
    });

    $("#id_avatar").change(function() {
        if ($("#id_avatar").val() !== "") {
          $('#avatar-picker').children('span').html($("#id_avatar")[0].files[0].name)
        }
    });
})