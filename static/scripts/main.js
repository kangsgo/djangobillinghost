$( document ).ready( function() {
    'use strict';

    /* ==========================================================================
     SEARCH
     ========================================================================== */
    $('a[href="#search"]').on('click', function(event) {
        event.preventDefault();
        $(".top-search").slideToggle();
        $('.top-search form input[type="search"]').focus();
    });

    /* ==========================================================================
     OWL-CAROUSEL
     ========================================================================== */
    // Quote
    var owlQuote = $( "#quote" );

    owlQuote.owlCarousel( {
        items: 1,
        loop: true,
        margin: 20,
        dots: false
    } );

    // Testimonials1
    var owlTesti = $( "#testi-carousel" );

    owlTesti.owlCarousel( {
        items: 1,
        loop: true,
        margin: 20
    } );

    // Testimonials2
    var owlTesti2 = $( "#testi-carousel2" );

    owlTesti2.owlCarousel( {
        items: 1,
        loop: true,
        margin: 20
    } );

    // Clients
    var owlClients = $( "#carousel-client" );

    owlClients.owlCarousel( {
        items: 6,
        loop: true,
        margin: 40,
        dots: false,
        autoplay: 2000,
        autoplayHoverPause: true,
        responsive:{
            0:{
                items:2,
            },
            600:{
                items:4,
            },
            1000:{
                items:6,
            }
        }
    } );

    /* ==========================================================================
     Slick
     ========================================================================== */
    var $carouseldn = $(".carousel-dn");
    $carouseldn.slick({
        infinite: true,
        slidesToShow: 3,
        slidesToScroll: 3,
        responsive: [
            {
                breakpoint: 1024,
                settings: {
                    slidesToShow: 3,
                    slidesToScroll: 3,
                    infinite: true,
                    dots: true
                }
            },
            {
                breakpoint: 768,
                settings: {
                    slidesToShow: 2,
                    slidesToScroll: 2
                }
            },
            {
                breakpoint: 480,
                settings: {
                    slidesToShow: 1,
                    slidesToScroll: 1
                }
            }
        ]
    });

    var $carouseldn2 = $(".carousel-dn2");
    $carouseldn2.slick({
        infinite: true,
        slidesToShow: 3,
        slidesToScroll: 3,
        dots: true,
        responsive: [
            {
                breakpoint: 1024,
                settings: {
                    slidesToShow: 3,
                    slidesToScroll: 3,
                    infinite: true,
                    dots: true
                }
            },
            {
                breakpoint: 768,
                settings: {
                    slidesToShow: 2,
                    slidesToScroll: 2
                }
            },
            {
                breakpoint: 480,
                settings: {
                    slidesToShow: 1,
                    slidesToScroll: 1
                }
            }
        ]
    });

    /* ==========================================================================
     SLIDER FILTER
     ========================================================================== */
    // 3 col in row
    $('.carousel-main').slick({
        slidesToShow: 3,
        slidesToScroll: 3,
        arrows: true,
        infinite: true,
        responsive: [
    {
                breakpoint: 1024,
                settings: {
                    slidesToShow: 3,
                    slidesToScroll: 3,
                }
            },
            {
                breakpoint: 768,
                settings: {
                    slidesToShow: 2,
                    slidesToScroll: 2
                }
            },
            {
                breakpoint: 480,
                settings: {
                    slidesToShow: 1,
                    slidesToScroll: 1
                }
            }
        ]
    });

    var filtered = false;

    $('.all-filters').on('click', function () {
        $('.active').removeClass('active');
        $('.all-filters').addClass('active');
        $('.carousel-main').slick('slickUnfilter');
        filtered = false;
    });

    $('.branding-filter').on('click', function () {
        $('.carousel-main').slick('slickUnfilter');
        $('.carousel-main').slick('slickFilter','.branding');
        $('.active').removeClass('active');
        $('.branding-filter').addClass('active');
        filtered = true;
    });

    $('.photo-filter').on('click', function () {
        $('.carousel-main').slick('slickUnfilter');
        $('.carousel-main').slick('slickFilter','.photo');
        $('.active').removeClass('active');
        $('.photo-filter').addClass('active');
        filtered = true;
    });

    $('.illustration-filter').on('click', function () {
        $('.carousel-main').slick('slickUnfilter');
        $('.carousel-main').slick('slickFilter','.illustration');
        $('.active').removeClass('active');
        $('.illustration-filter').addClass('active');
        filtered = true;
    });

    $('.web-filter').on('click', function () {
        $('.carousel-main').slick('slickUnfilter');
        $('.carousel-main').slick('slickFilter','.web');
        $('.active').removeClass('active');
        $('.web-filter').addClass('active');
        filtered = true;
    });

    // 4 col in row
    $('.carousel-main-4col').slick({
        slidesToShow: 4,
        slidesToScroll: 4,
        arrows: true,
        infinite: true,
        responsive: [
            {
                breakpoint: 1024,
                settings: {
                    slidesToShow: 4,
                    slidesToScroll: 4,
                }
            },
            {
                breakpoint: 768,
                settings: {
                    slidesToShow: 2,
                    slidesToScroll: 2
                }
            },
            {
                breakpoint: 480,
                settings: {
                    slidesToShow: 1,
                    slidesToScroll: 1
                }
            }
        ]
    });

    var filtered = false;

    $('.all-filters').on('click', function () {
        $('.active').removeClass('active');
        $('.all-filters').addClass('active');
        $('.carousel-main-4col').slick('slickUnfilter');
        filtered = false;
    });

    $('.branding-filter').on('click', function () {
        $('.carousel-main-4col').slick('slickUnfilter');
        $('.carousel-main-4col').slick('slickFilter','.branding');
        $('.active').removeClass('active');
        $('.branding-filter').addClass('active');
        filtered = true;
    });

    $('.photo-filter').on('click', function () {
        $('.carousel-main-4col').slick('slickUnfilter');
        $('.carousel-main-4col').slick('slickFilter','.photo');
        $('.active').removeClass('active');
        $('.photo-filter').addClass('active');
        filtered = true;
    });

    $('.illustration-filter').on('click', function () {
        $('.carousel-main-4col').slick('slickUnfilter');
        $('.carousel-main-4col').slick('slickFilter','.illustration');
        $('.active').removeClass('active');
        $('.illustration-filter').addClass('active');
        filtered = true;
    });

    $('.web-filter').on('click', function () {
        $('.carousel-main-4col').slick('slickUnfilter');
        $('.carousel-main-4col').slick('slickFilter','.web');
        $('.active').removeClass('active');
        $('.web-filter').addClass('active');
        filtered = true;
    });

    /* ==========================================================================
     ISOTOPE: Portfolio, Blog masonry
     ========================================================================== */
    // Gallery masonry
    var $galleryLightbox = $('.gallery-lightbox' ).isotope( {
        itemSelector: '.gallery-item',
        percentPosition: true,
    } );

    $galleryLightbox.imagesLoaded().progress( function() {
        $galleryLightbox.isotope('layout');
    });

    // Blog masonry
    var $blogGrid = $('.blog-grid-masonry' ).isotope( {
        itemSelector: '.post',
        percentPosition: true,
    } );

    $blogGrid.imagesLoaded().progress( function() {
        $blogGrid.isotope('layout');
    });

    // Portfolio - Home
    var $folioGrid2 = $('.folio-main-5col');
    $folioGrid2.isotope({
        layoutMode: "masonry",
        masonry: {
            columnWidth: '.folio-main-item_sizer'
        },
        itemSelector: '.folio-main-item',
        transitionDuration: '0.8s'
    });
    $folioGrid2.imagesLoaded().progress( function() {
        $folioGrid2.isotope('layout');
    });

    // Home 11
    var $folioGrid4 = $('.folio-main-4col-3inrow');
    $folioGrid4.isotope({
        layoutMode: "masonry",
        masonry: {
            columnWidth: '.folio-main-item_sizer'
        },
        itemSelector: '.folio-main-item',
        transitionDuration: '0.8s'
    });
    $folioGrid4.imagesLoaded().progress( function() {
        $folioGrid4.isotope('layout');
    });

    // Portfolio
    var $folioGrid = $('.folio-main-grid');
    $folioGrid.isotope({
        layoutMode: "masonry",
        itemSelector: '.folio-main-item',
        transitionDuration: '0.8s'
    });

    $folioGrid.imagesLoaded().progress( function() {
        $folioGrid.isotope('layout');
    });

    var $optionSets = $('.folio-main-filter'),
        $optionLinks = $optionSets.find('a');
    $optionLinks.on('click', function() {
        var $this = $(this);
        // don't proceed if already selected
        if ($this.hasClass('active')) {
            return false;
        }
        var $optionSet = $this.parents('.folio-main-filter');
        $optionSet.find('.active').removeClass('active');
        $this.addClass('active');
        // make option object dynamically, i.e. { filter: '.my-filter-class' }
        var options = {},
            key = $optionSet.attr('data-option-key'),
            value = $this.attr('data-option-value');

        // parse 'false' as false boolean
        value = value === 'false' ? false : value;
        options[key] = value;
        if (key === 'layoutMode' && typeof changeLayoutMode === 'function') {
            changeLayoutMode($this, options);
        } else {
            // otherwise, apply new options
            $folioGrid.isotope(options);
        }
        return false;
    });

    /* ==========================================================================
     COUNTER
     ========================================================================== */
    var $counter = $(".counter");
    $counter.counterUp( {
        delay: 10,
        time: 1000
    } );

    /* ==========================================================================
     COUNTDOWN CLOCK
     ========================================================================== */
    $( "#ctimer" )
        .countdown( "2016/08/08", function( event ) {
            $( this ).html(
                event.strftime( '<div class="time">%D<span>Days</span></div><div class="time"> %H<span>Hour</span></div><div class="time"> %M<span>Minutes</span></div><div class="time"> %S<span>Seconds</span></div>' )
            );
        } );

    $( "#ctimer2" )
        .countdown( "2016/07/01", function( event ) {
            $( this ).html(
                event.strftime( '<div class="time">%D<span>Days</span></div><em>:</em><div class="time">%H<span>Hour</span></div><em>:</em><div class="time">%M<span>Minutes</span></div><em>:</em><div class="time">%S<span>Seconds</span></div>' )
            );
        } );


    /* ==========================================================================
     LightGallery
     ========================================================================== */
    // Gallery Lightbox
    var $galleryLightbox = $(".gallery-lightbox");
    $galleryLightbox.lightGallery( {
        thumbnail: true
    } );

    // Photo Stream
    var $photoStream = $(".gallery");
    $photoStream.lightGallery( {
        thumbnail: true
    } );

    // Portfolio gallery
    var $folioGallery = $(".folio-gallery");
    $folioGallery.lightGallery( {
        thumbnail: true
    } );


    // Product single
    var $imageProduct = $("#imageProduct");
    $imageProduct.lightSlider({
        addClass : 'imageProduct',
        gallery:true,
        item:1,
        loop:true,
        thumbItem:7,
        slideMargin:0,
        enableDrag: false,
        currentPagerPosition:'left',
        onSliderLoad: function(el) {
            el.lightGallery({
                selector: '#imageProduct .lslide'
            });
        }
    });

    /* ==========================================================================
     Magnific-Popup
     ========================================================================== */

    // Product Preview
    var $productReview = $(".product-review");
    $productReview.magnificPopup({
        type: 'image'
        // other options
    });

    /* ==========================================================================
     Checkout - Ship to different address checkbox
     ========================================================================== */
    var $shipDifferentCheckbox = $("input#ship-different-checkbox");
    $shipDifferentCheckbox.on('change', function(){
        var $this = $(this),
            $btn = $( $this.closest('.customCollapse').data('href') );

        if ($this.is(":checked") ) {
            $btn
                .addClass('in')
                .css('height', 'auto');
        } else {
            $btn
                .css('height', 'auto')
                .removeClass('in');
        }
    });

    /* ==========================================================================
     Gmap3
     ========================================================================== */
    if($('#map' ).length > 0) {
        $( '#map' )
            .gmap3( {
                center: [ 43.059872, -76.155451 ],
                zoom: 13,
                mapTypeId: "style1",
                mapTypeControl: false,
            } )
            .marker({
                position:[43.059872, -76.155451],
                icon: '/images/marker.png'
            })
            .styledmaptype(
                "style1",
                [{"featureType":"all","elementType":"labels.text.fill","stylers":[{"saturation":36},{"color":"#000000"},{"lightness":70}]},{"featureType":"all","elementType":"labels.text.stroke","stylers":[{"visibility":"on"},{"color":"#000000"},{"lightness":16}]},{"featureType":"all","elementType":"labels.icon","stylers":[{"visibility":"off"}]},{"featureType":"administrative","elementType":"geometry.fill","stylers":[{"color":"#000000"},{"lightness":20}]},{"featureType":"administrative","elementType":"geometry.stroke","stylers":[{"color":"#000000"},{"lightness":17},{"weight":1.2}]},{"featureType":"landscape","elementType":"geometry","stylers":[{"color":"#000000"},{"lightness":20}]},{"featureType":"poi","elementType":"geometry","stylers":[{"color":"#000000"},{"lightness":21}]},{"featureType":"road.highway","elementType":"geometry.fill","stylers":[{"color":"#000000"},{"lightness":17}]},{"featureType":"road.highway","elementType":"geometry.stroke","stylers":[{"color":"#000000"},{"lightness":29},{"weight":0.2}]},{"featureType":"road.arterial","elementType":"geometry","stylers":[{"color":"#000000"},{"lightness":18}]},{"featureType":"road.local","elementType":"geometry","stylers":[{"color":"#000000"},{"lightness":16}]},{"featureType":"transit","elementType":"geometry","stylers":[{"color":"#000000"},{"lightness":19}]},{"featureType":"water","elementType":"geometry","stylers":[{"color":"#000000"},{"lightness":17}]}],
                {name: "Style 1"}
        )
        ;
    }

    /* ==========================================================================
     MOBILE MENU
     ========================================================================== */
    var slideout = new Slideout({
        'panel': document.getElementById('main'),
        'menu': document.getElementById('menu-slideout'),
        'side': 'right',
        'padding': 256,
        'tolerance': 70,
        'drag': false
    });

    // Toggle button
    if ($('#open-left' ).length > 0) {
        document.querySelector( '#open-left' ).addEventListener( 'click', function() {
            slideout.toggle();
        } );
    }

    $('#main' ).on('click', function(e){
        if ($(e.target).closest('#open-left').length == 0) {
            if (slideout._opened) {
                e.preventDefault();
            }
            slideout.close();
        }
    });

    // Expand
    var $menu = $( '#menu-slideout' );

    $menu.find( '.sub-menu-toggle' ).on( 'click', function( e ) {
        var subMenu = $( this ).next();

        if ( subMenu.css( 'display' ) == 'block' ) {
            subMenu.css( 'display', 'block' ).slideUp().parent().removeClass( 'expand' );
        } else {
            subMenu.css( 'display', 'none' ).slideDown().parent().addClass( 'expand' );
        }
        e.stopPropagation();
    } );

    /* ==========================================================================
     Full Screen Vertical Scroller
     ========================================================================== */
    $('#fullpage').fullpage({
        scrollOverflow: true
    });

    /* ==========================================================================
     ScrollUp
     ========================================================================== */
    $.scrollUp({
        scrollName: 'scrollUp', // Element ID
        topDistance: '300', // Distance from top before showing element (px)
        topSpeed: 300, // Speed back to top (ms)
        animation: 'fade', // Fade, slide, none
        animationInSpeed: 300, // Animation in speed (ms)
        animationOutSpeed: 300, // Animation out speed (ms)
        scrollText: '<span class="pe-7s-angle-up"></span>', // Text for element
        activeOverlay: false, // Set CSS color to display scrollUp active point, e.g '#00FFFF'
    });

} );
