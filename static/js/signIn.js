var csrftoken = getCookie('csrftoken');
var beprevented = false;

// If user wants to login from password_change page login modal shows
if ($('#login_from_pass_change').val() == 'True'){
    $('#loginModal').modal();
}

//At login from username_or_email whitespaces deleted
$("#id_username_or_email").change(function() {
    var id_username_or_email = $(this).val().trim();
    $(this).val(id_username_or_email);
});

//At login form is 'enter' pushed login_button click event is called
$('#id_username_or_email').on('keypress', function(event) {
    if(event.which == 13 && $(this).val() != "") {
        $('#login_button').click();
    }
});
$('#id_password').on('keypress', function(event){
    if(event.which == 13 && $(this).val() != "") {
        $('#login_button').click();
    }
});

//Sends the data to the server to check if those were correct
//Returns true/false to be the value of 'beprevented'
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

//Sends the user's data to the server
$('.loginform').on('submit', function(event) {
//If the user's auth failed submit prevented
    if (beprevented){
        event.preventDefault();
    }
    else{
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
    }
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
