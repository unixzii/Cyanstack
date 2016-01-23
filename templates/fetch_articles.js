{% autoescape None %}
(function () {
	var article_item_htmls = [
		{% for index, html in enumerate(htmls) %}
			{% if not index == 0 %}
				,
			{% end%}
			{{html}}
		{% end %}
	];
	var el = jQuery('#articles-container');
	el.empty();
	for (var i = 0; i < article_item_htmls.length; i++) {
		el.append(article_item_htmls[i]);
	}
	jQuery('#loading-indicator').hide();
	jQuery('#end-hint').text('/* {{hint}} */');
	{% if nav_type == 2 or nav_type == -1 %}
		jQuery('#prev-btn').removeClass('hide');
	{% else %}
		jQuery('#prev-btn').addClass('hide');
	{% end %}
	{% if nav_type == 2 or nav_type == 1 %}
		jQuery('#next-btn').removeClass('hide');
	{% else %}
		jQuery('#next-btn').addClass('hide');
	{% end %}
	currentPage = {{page}};
})();