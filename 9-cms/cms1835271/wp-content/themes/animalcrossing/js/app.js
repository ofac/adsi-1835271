$(document).ready(function() {
	$('body').on('click', '.leaf', function(event) {
		event.preventDefault();
		$('div.menu-top-menu-container').toggleClass('open');
	});
});