//This function is responsible for checking the given username is either in the database or not
//It shows a message to the user if username exists and prevent from submitting if username is taken
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
			}
			else{
				$('#usernameAlert').fadeOut();
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
		dataType: 'json',
		success: function(data) {
			if (data.email_is_taken) {
				$('#emailAlert').fadeIn();
			}
			else{
				$('#emailAlert').fadeOut();
			}
		}
	});
});
