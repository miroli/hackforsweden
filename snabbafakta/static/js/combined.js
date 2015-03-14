$('.puff img').on('click', function(e) {
	var $target = $(e.target)
			href = $target.parent().find('a').attr('href');

	location.href = href;
});