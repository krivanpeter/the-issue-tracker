var csrftoken = getCookie('csrftoken');
var beprevented = false;

if ($('#login_from_pass_change').val() == 'True'){
    $('#loginModal').modal();
}

$("#id_username_or_email").change(function() {
    var id_username_or_email = $(this).val().trim();
    $(this).val(id_username_or_email);
});

$('#id_username_or_email').on('keypress', function(event) {
    if(e.which == 13) {
        $('#login_button').click();
    }
});
$('#id_password').on('keypress', function(event){
    if(e.which == 13) {
        $('#login_button').click();
    }
});

$('#login_button').on('click', function(event) {
    var username_or_email = $("#id_username_or_email").val().trim();
    var password = $('#id_password').val();
        $.ajax({
            data: {
                'username_or_email': username_or_email,
                'password': password,
                csrftoken: csrftoken
            },
            type: 'POST',
            url: '/accounts/check_userdata/',
            async: false,
            success: function(data) {
                if (data.username_or_password_error) {
                $('#username_or_password_error').fadeIn();
                    beprevented = true;
                }
                else {
                    beprevented = false;
                }
            }
        });
});


$('.loginform').on('submit', function(event) {
    if (beprevented){
        event.preventDefault();
    }
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
    });
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

$.ajaxSetup({
    beforeSend: function(xhr, settings) {
        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    }
});
