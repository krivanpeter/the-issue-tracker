/*After page loaded, run the ,,changeNavBar()" function*/
$(document).ready(function() {
    changeNavBar();
})
/*If window was resized, run the ,,changeNavBar()" function*/
$(window).resize(function() {
    changeNavBar();
});

/*Function to change the navbar behavior depends on the size of the screen*/
function changeNavBar() {
    $(document).on("scroll", function() {
        if ($(window).width() >= 768) {
            if ($(window).scrollTop() === 0) {
                $('.navbar').addClass('navbar-transparent');
                $('.navbar').removeClass('navbar-white');
                $('.navbar-brand').addClass('logo');
                $('.navbar-brand').removeClass('logo-transparent');
                $('.nav-item button').addClass('white-text');
                $('.nav-item button').removeClass('black-text');
                $('.nav-link i').addClass('white-text');
                $('.nav-link i').removeClass('orange-fa');
            }
            else {
                $('.navbar').removeClass('navbar-transparent');
                $('.navbar').addClass('navbar-white');
                $('.navbar-brand').removeClass('logo');
                $('.navbar-brand').addClass('logo-transparent');
                $('.nav-item button').removeClass('white-text');
                $('.nav-item button').addClass('black-text');
                $('.nav-link i').removeClass('white-text');
                $('.nav-link i').addClass('orange-fa');
            }
        }
        else {
            $('.navbar').addClass('navbar-transparent');
            $('.navbar').removeClass('navbar-white');
            $('.navbar-brand').addClass('logo');
            $('.navbar-brand').removeClass('logo-transparent');
            $('.nav-item button').addClass('white-text');
            $('.nav-item button').removeClass('black-text');
            $('.nav-link i').addClass('white-text');
            $('.nav-link i').removeClass('black-text');
        }
    });
}
