//This function is responsible for checking the given username and e-mail address are either in the database or not
//It shows a message to the user if username and/or email exist(s) and prevent from submitting if username is taken
var usernameTaken = false;
var emailTaken = false;
$("#id_username").change(function() {
	var username = $(this).val();
	$.ajax({
		url: '/accounts/check_username/',
		data: {
			'username': username
		},
		dataType: 'json',
		success: function(data) {
			if (data.username_is_taken) {
				$('#usernameAlert').fadeIn();
				usernameTaken = true;
			}
			else{
				$('#usernameAlert').fadeOut();
				usernameTaken = false;
			}
		}
	});
});

$("#id_email").change(function() {
	var email = $(this).val();
	console.log(email);
	$.ajax({
		url: '/accounts/check_email/',
		data: {
			'email': email
		},
		dataType: 'JSON',
		success: function(data) {
			if (data.email_is_taken) {
				$('#emailAlert').fadeIn();
				emailTaken = true;
			}
			else{
				$('#emailAlert').fadeOut();
				emailTaken = false;
			}
		}
	});
});

function regFormSubmitChecker(){
	if (usernameTaken && emailTaken){
		event.preventDefault();
	}
}
