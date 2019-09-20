$(document).ready(function() {
    $('#reported-bugs-btn').on('click', function(event) {
        $(this).addClass("btn-dark")
        $('#upvoted-bugs-btn').removeClass("btn-dark");
        $('#asked-features-btn').removeClass("btn-dark");
        $('#upvoted-features-btn').removeClass("btn-dark");

        $('#profile-reported-bugs').show();
        $('#profile-upvoted-bugs').hide();
        $('#profile-asked-features').hide();
        $('#profile-upvoted-features').hide();
    });
    $('#upvoted-bugs-btn').on('click', function(event) {
        $(this).addClass("btn-dark")
        $('#reported-bugs-btn').removeClass("btn-dark");
        $('#asked-features-btn').removeClass("btn-dark");
        $('#upvoted-features-btn').removeClass("btn-dark");

        $('#profile-reported-bugs').hide();
        $('#profile-upvoted-bugs').show();
        $('#profile-asked-features').hide();
        $('#profile-upvoted-features').hide();
    });
    $('#asked-features-btn').on('click', function(event) {
        $(this).addClass("btn-dark")
        $('#reported-bugs-btn').removeClass("btn-dark");
        $('#upvoted-bugs-btn').removeClass("btn-dark");
        $('#upvoted-features-btn').removeClass("btn-dark");

        $('#profile-reported-bugs').hide();
        $('#profile-upvoted-bugs').hide();
        $('#profile-asked-features').show();
        $('#profile-upvoted-features').hide();
    });
    $('#upvoted-features-btn').on('click', function(event) {
        $(this).addClass("btn-dark")
        $('#reported-bugs-btn').removeClass("btn-dark");
        $('#upvoted-bugs-btn').removeClass("btn-dark");
        $('#asked-features-btn').removeClass("btn-dark");

        $('#profile-reported-bugs').hide();
        $('#profile-upvoted-bugs').hide();
        $('#profile-asked-features').hide();
        $('#profile-upvoted-features').show();
    });
});