var timer;

function parse_JSON(res){
	var htmString = '';
	var note_body = '';
	for (var i = 0; i < res.length; i++){
		if (res[i].description == null){
			note_body = '';
		} else {
			note_body = res[i].description;
		}
		htmString += '<div class="note"><div><h2>'+res[i].title+'</h2><form class="delete" id="'+res[i].id+'"><input type="submit" value="Delete"></form></div>';
		htmString += '<form class="old_note"><input type="hidden" name="note_id" value="'+res[i].id+'"><textarea class="note_desc" name="note_desc" placeholder="Enter description here">'+note_body+'</textarea></form></div>';
	}
	$('#notes').html(htmString);
}

$(document).ready(function(){

	function readyPage(){
		$.get('/index_json', function(res){
			parse_JSON(res);
		}, 'json');
	}

	readyPage();
	

	$('#new_note').submit(function(){
		$.post('index_json/create', $(this).serialize(), function(res){
			parse_JSON(res);
		}, 'json');
		$('#new_title').val('');
		return false;
	});

	$('#notes').on('submit', '.delete', function(){
		delete_id = $(this).attr('id');
		route = '/'+delete_id+'/delete';
		$.get(route, function(res){
			parse_JSON(res);
		}, 'json');
		return false;
	})

	$('#notes').on('keydown', 'textarea', function(){
		this_note = $(this);
		if (timer) clearTimeout(timer);
		timer = setTimeout(function(){
			timer = null;
			this_note.parent().submit();
			this_note.addClass('saved');
			setTimeout(function(){this_note.removeClass('saved');}, 500);
		}, 1000);
	});

	$('#notes').on('submit', '.old_note', function(){
		$.post('/index_json/update', $(this).serialize(), false);
		return false;
	});

})