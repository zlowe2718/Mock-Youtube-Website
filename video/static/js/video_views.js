$(document).ready(function() {
	var total_time_watched = 0;
	var timer;
	var video = $('#video');
	var sent_request = false;
	video.on("play", startPlaying);
	video.on("pause", stopPlaying);

	function startPlaying() {
		var duration = video.prop("duration");
		timer = setInterval(function() {
			total_time_watched += 1;
			if (!sent_request && total_time_watched >= .5 * duration) {
				$.ajax({
					type: "POST",
					data: {'content': 'video-view', 'csrfmiddlewaretoken': window.CSRF_TOKEN},
					datatype: "json",
					success: function(response) {
						var view_count = $('.view-counter').text();
						$('.view-counter').text(parseInt(view_count) + 1);
						sent_request = true;
					}
				})
			}
		}, 1000);
	}

	function stopPlaying() {
		if (timer) clearInterval(timer);
	}
});