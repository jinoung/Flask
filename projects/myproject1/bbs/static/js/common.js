// http://getbootstrap.com/javascript/#tooltips
$('body').tooltip({
	selector: '[data-toggle=tooltip]',
	placement : 'auto top',
	html: 'true',
	container: 'body',
});

// feedback messages
var feedback = (function() {
    "use strict";

    var elem,
        hideHandler,
        that = {};

    that.init = function(options) {
        elem = $(options.selector);
    };

    that.show = function(text) {
        clearTimeout(hideHandler);

        elem.find("span").html(text);
        elem.delay(100).fadeIn().delay(500).fadeOut();
    };

    return that;
}());

$(function () {
    feedback.init({
        "selector": ".rb-feedback "
    });
});



// jQuery.imageCaption.js : https://github.com/andreasnymark/jQuery.imageCaption

(function($){ 
	$.fn.imageCaption = function(options) {
		var defaults = {  
		    figure: '<figure>',
		    figcaption: '<figcaption>'
		};  
		var options = $.extend(defaults, options); 
		return this.each(function() { 
			var o = $(this);
			var alt = o.attr('alt');
			var classes = o.attr('class');
			var caption = $(options.figcaption).text(alt);
			o
				.removeClass()
				.wrap(options.figure)
				.parent()
				.addClass(classes)
				.append(caption);
		});
	}
})(jQuery);