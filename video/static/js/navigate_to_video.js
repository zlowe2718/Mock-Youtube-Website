$(document).ready(function() {
	var searchbar = $('#searchbar');
	var options = $(".options-list li");
	var menu_icon = $(".nav-img")
	var menu = $(".col-sm-2")
	var menu_dom = document.getElementsByClassName("col-sm-2")[0]
	var menu_item_dom = document.getElementsByClassName("menu")[0]
	var dimmer = $(".dimmer")
	$(searchbar).focusin(function() {
		$(".dropdown-box").css("display", "block");
	});
	$(".options-list").on("mousedown", "li" , function() {
		window.location = $(this).attr("data-val");
	});
	$(searchbar).not("options-list li").focusout(function() {
		$(".dropdown-box").css("display", "none");
	});
	$("body").click(function(e) {
		if($(e.target).is(".nav-img") || (menu_dom.contains(e.target) && !menu_item_dom.contains(e.target))) {
			$(dimmer).css("display", "block");
			$(menu).css("display", "block");			
		} else {
			$(menu).css("display", "none");
			$(dimmer).css("display", "none");
		}
	})
});