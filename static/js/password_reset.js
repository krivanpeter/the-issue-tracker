var csrftoken = getCookie('csrftoken');

//Sends the email address to the server
//Then shows ,,email sent" modal
$('.forgottenpassform').on('submit', function(event) {
    var email = $('.forgottenpassform').children('#id_email').val();
    var reset_password = 'reset_password';
    $.ajax({
        data: {
            'reset_password': reset_password,
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

//CSRFToken acquiring (code from Django's webpage)
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

$.ajaxSetup({
    beforeSend: function(xhr, settings) {
        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    }
});
