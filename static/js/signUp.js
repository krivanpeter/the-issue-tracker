//This function is responsible for checking the given username and e-mail address are either in the database or not
//It shows a message to the user if username and/or email exist(s) and prevent from submitting if username is taken
var usernameTaken = false;
var emailTaken = false;
var passwordDifferent = false;

//It sends the selected username to the server, if it is already taken shows an error
$("#id_username").change(function() {
	var username = $(this).val().trim();
	$(this).val(username);
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

//It sends the selected email address to the server, if it is already taken shows an error
$("#id_registration_email").change(function() {
	var email = $(this).val().trim();
	$(this).val(email);
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

//Everytime the passwords change it calls the passwordIdentity() function
$("#id_password2").change(function() {
	passwordIdentity();
});

$("#id_password1").change(function() {
	passwordIdentity();
});

//Checks if the 2 passwords are the same, if not shows an error
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

//When registration form submitted, it prevents the submit if username/email address is/are taken,
//or the passwords are different
function regFormSubmitChecker() {
	if (usernameTaken || emailTaken || passwordDifferent) {
		event.preventDefault();
	}
}
