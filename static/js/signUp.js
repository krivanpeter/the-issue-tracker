//This function is responsible for checking the given username and e-mail address are either in the database or not
//It shows a message to the user if username and/or email exist(s) and prevent from submitting if username is taken
var usernameTaken = false;
var emailTaken = false;
var passwordDifferent = false;

$("#id_username").change(function() {
	var username = $(this).val().trim();
	$.ajax({
		url: '/accounts/check_username/',
		data: {
			'username': username
		},
		dataType: 'JSON',
		success: function(data) {
			if (data.username_is_taken) {
				$('#usernameAlert').fadeIn();
				usernameTaken = true;
			}
			else {
				$('#usernameAlert').fadeOut();
				usernameTaken = false;
			}
		}
	});
});

$("#id_email").change(function() {
	var email = $(this).val().trim();
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
			else {
				$('#emailAlert').fadeOut();
				emailTaken = false;
			}
		}
	});
});

$("#id_password2").change(function() {
	passwordIdentity();
});

$("#id_password1").change(function() {
	passwordIdentity();
});

function passwordIdentity() {
	var password1 = $("#id_password1").val();
	var password2 = $("#id_password2").val();
	if (password1 != password2) {
		if (password2 != "") {
			$('#passwordAlert').fadeIn();
		}
		passwordDifferent = true;
	}
	else {
		$('#passwordAlert').fadeOut();
		passwordDifferent = false;
	}
}

function regFormSubmitChecker() {
	var username = $("#id_username").val().trim();
	if (usernameTaken || emailTaken || passwordDifferent || username == "") {
		event.preventDefault();
	}
}
