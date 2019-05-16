var csrftoken = getCookie('csrftoken');

$.ajaxSetup({
    beforeSend: function(xhr, settings) {
        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    }
});
$("#id_username_or_email").change(function() {
    var id_username_or_email = $(this).val().trim();
    $(this).val(id_username_or_email);
});

$('.loginform').on('submit', function(event) {
    var username_or_email = $('#id_username_or_email').val();
    var password = $('#id_password').val();
    $.ajax({
        data: {
            'username_or_email': username_or_email,
            'password': password,
            csrftoken: csrftoken
        },
        type: 'POST',
        url: '/accounts/login/',
        success: function(data) {
            console.log(data)
            if (data.username_or_password_error) {
                $('#username_or_password_error').fadeIn();
            }
            else {
                window.location.reload();
                $('#username_or_password_error').hide();
            }
        }
    })
    event.preventDefault();
});

function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}
