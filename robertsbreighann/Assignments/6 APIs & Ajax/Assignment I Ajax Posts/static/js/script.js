$(document).ready(function(){

	function getNotes(){
		$.get('/index_json', function(res){
			var htmlStr = '<!--';
			for (var i = 0; i < res.length; i++){
				htmlStr += '--><p class="post">' + res[i].post + '</p><!--';
			}
			htmlStr += '-->'
			$('#board').html(htmlStr);
			$('textarea').val('');
		}, 'json');
	}

	getNotes();

	$('form').submit(function(){
		$.post('/index_json/create', $(this).serialize(), function(res){
			var htmlStr = '<!--';
			for (var i = 0; i < res.length; i++){
				htmlStr += '--><p class="post">' + res[i].post + '</p><!--';
			}
			htmlStr += '-->'
			$('#board').html(htmlStr);
			$('textarea').val('');
		}, 'json');
		return false;
	})



})