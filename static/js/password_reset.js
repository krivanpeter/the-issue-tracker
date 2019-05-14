var csrftoken = getCookie('csrftoken');

$.ajaxSetup({
    beforeSend: function(xhr, settings) {
        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    }
});

$('.forgottenpassform').on('submit', function(event) {
    var email = $('.forgottenpassform').children('#id_email').val();
    $.ajax({
        data: {
            'email': email,
            csrftoken: csrftoken
        },
        type: 'POST',
        url: '/',
        success: function(data) {
            if (data.data = true) {
                $('#forgottenPasswordModal').modal('hide');
                $('#emailSendModal').modal();
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
