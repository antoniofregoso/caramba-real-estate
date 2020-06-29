odoo.define('real_estate.real_estate', function (require) {
'use strict';


var publicWidget = require('web.public.widget');
var Swiper = require('Swiper');

publicWidget.registry.js_get_services = publicWidget.Widget.extend({
    selector: '.re-swiper-container',
    
    start: function () {
    	var self = this;
    	var swiper = new Swiper('.re-swiper-container', {
    	      effect: 'coverflow',
    	      grabCursor: true,
    	      centeredSlides: true,
    	      slidesPerView: 'auto',
    	      coverflowEffect: {
    	        rotate: 50,
    	        stretch: 0,
    	        depth: 100,
    	        modifier: 1,
    	        slideShadows : true,
    	      },
    	      pagination: {
    	        el: '.swiper-pagination',
    	      },
    	    });
    },
    
});

})