/*After page loaded, run the ,,changeNavBar()" function*/
$(document).ready(function() {
    changeNavBar();
})
/*If window resized, run the ,,changeNavBar()" function*/
$(window).resize(function () { 
    changeNavBar();
});

/*Function to change the navbar behavior depends on the size of the screen*/
function changeNavBar() {
    if ($(window).width() > 768) {
        $(document).scroll(function() {
            if ($(window).scrollTop() === 0) {
                $('.navbar').addClass('navbar-transparent');
                $('.navbar').removeClass('navbar-white');
                $('.navbar-brand').addClass('logo');
                $('.navbar-brand').removeClass('logo-transparent');
                $('.nav-item a').addClass('white-text');
                $('.nav-item a').removeClass('black-text');
                $('.nav-link i').addClass('white-text');
                $('.nav-link i').removeClass('black-text');
            }
            else {
                $('.navbar').addClass('navbar-white');
                $('.navbar').removeClass('navbar-transparent');
                $('.navbar-brand').addClass('logo-transparent');
                $('.navbar-brand').removeClass('logo');
                $('.nav-item a').addClass('black-text');
                $('.nav-item a').removeClass('white-text');
                $('.nav-link i').addClass('black-text');
                $('.nav-link i').removeClass('white-text');
            }
        });
    }
}
