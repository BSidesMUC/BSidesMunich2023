$(document).ready(function(){

	$("#portfolio-contant-active").mixItUp();

	$( ".owl-carousel" ).each(function( index ) {
		$( this ).owlCarousel({
			singleItem:true,
			items:1,
			autoplay:true,
			autoplayTimeout:3000,
			loop:true,
			autoplayHoverPause:true
		});
	});

	// Counter
	$('.counter').counterUp({
        delay: 10,
        time: 1000
    });

});




