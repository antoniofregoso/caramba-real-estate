odoo.define('real_estate.real_estate', function (require) {
'use strict';


var publicWidget = require('web.public.widget');

publicWidget.registry.realEstateUnits = publicWidget.Widget.extend({
    selector: '#re-units',
    
   start: function () {
    	var self = this;
    	var config = document.getElementById('re-units');
    	// base swipper
    	var swiperStyle = {
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
    	      }}
    	// Navigation
    	if (config.dataset.navigation=='True'){
    		swiperStyle['navigation']= {
  	          nextEl: '.swiper-button-next',
	          prevEl: '.swiper-button-prev',
	        }
    	}    	
    	//Pagination
    	if (config.dataset.pagination=='numbered'){
    		swiperStyle['pagination'] = {
    	    	  el: '.swiper-pagination',
                  clickable: true,
                  renderBullet: function (index, className) {
    	          return '<span class="' + className + '">' + (index + 1) + '</span>';
    	        },};    		
    	} else if (config.dataset.pagination=='dots') {
    		swiperStyle['pagination'] = {
    		        el: '.swiper-pagination',
    	      };
    	} else if (config.dataset.pagination=='progress') {
    		swiperStyle['pagination'] = {
    		        el: '.swiper-pagination',
    		        type: 'progressbar',
    	      };
    	} else if (config.dataset.pagination=='fraction') {
    		swiperStyle['pagination'] = {
    		        el: '.swiper-pagination',
    		        type: 'fraction',
    	      };
    	} else if (config.dataset.pagination=='scrollbar') {
    		swiperStyle['pagination'] = {
    				el: '.swiper-scrollbar',
    		        hide: true,
    	      };
    	}
    	
    	var swiper = new Swiper('.re-units', 
    			swiperStyle);
    },
    
});

})