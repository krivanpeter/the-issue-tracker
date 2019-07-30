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
