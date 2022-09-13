$(document).ready(function() {
	var searchbar = $('#searchbar');
	$(searchbar).on('keyup', function() {
		DisplayDropdown(searchbar.val());
	});

	function DisplayDropdown(video_str) {
		var video_list = getVideos(video_str);
		$('#dropdown').attr('size', $('#dropdown option').length);
	};

	function getVideos(video_str) {
		//Make Ajax call here and return response
		if (!!video_str) {
			$.ajax({
				type: "POST",
				data: {'content': 'search-video', 'search-text': video_str, 'csrfmiddlewaretoken': window.CSRF_TOKEN},
				datatype: "json",
				success: function(response) {
					//What do I want to do once Ajax is successful? update the options?
					var options = $('.options-list li')
					for (let i = 0; i < options.length; i++) {
						options[i].remove()
					}
					for (const video of response.video_list) {
						addOption(video.video, video.url);
					};
					
				}
			});
		};
	};

	function addOption(video_name, url) {
		var dropdown = $('.options-list');
		dropdown.append($("<li>").text(video_name).attr('data-val', url));		
	};
});