var App = {
    init: function() {
        var path = window.location.pathname;
        var path_a = path.split('/');
        var mode = path_a[1];

        switch (mode) {
            case '':
                window.setTimeout(App.pageHome, 100);
                break;
            default:
        }
    },

    pageHome: function() {
        // EZ EZ EZ NAV
        $('ul.nav a').bind('click',function(event){
            var $anchor = $(this);

            if ($(this).attr('href') == '#home') {
                $('html, body').animate({scrollTop:0}, 'slow');
                return false;
            }

            $('html, body').stop().animate({
                scrollTop: $($anchor.attr('href')).offset().top
            }, 1500,'easeInOutExpo');
            event.preventDefault();
        });

        $('#mainCarousel').carousel({
            interval: false
        });

        $('#photosCarousel').carousel({
            interval: false
        });

        $('#bridesmaidsCarousel').carousel({
            interval: false
        });

        $('#groomsmenCarousel').carousel({
            interval: false
        });

    },
}

$(document).ready(function() {
    App.init();
});
