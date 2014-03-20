$(document).ready(function(){
	//initial menuitem form

	selected = $("#id_parent").val()
	//initial menuitem selectini
	$.ajax({
		type:"GET",
		url:"/ajax/menuitem/?menu_id="+$("#id_menu").val(),
		dataType:'json',
		success:function(data,textStatus){
			var menuitem_select = $("#id_parent");
			menuitem_select.empty();
			if (data.length >= 0){
					menuitem_select.append("<option value selected = 'selected'>---------</option>");
				for (i = 0;i<data.length; i++){
					option = "<option value="+data[i].value+">"+data[i].text+"</option>";
					menuitem_select.append(option);
				}
			if ($('#id_name').val().length > 0){
				menuitem_select.val(selected);
			}

			}
		}
	});



	$('#id_menu').change(function(){
		$.ajax({
			type:"GET",
			url:"/ajax/menuitem/?menu_id="+$(this).val(),
			dataType:'json',
			success:function(data,textStatus){
				var menuitem_select = $("#id_parent");
				menuitem_select.empty();
				if (data.length >= 0){
						menuitem_select.append("<option value selected = 'selected'>---------</option>");
					for (i = 0;i<data.length; i++){
						option = "<option value="+data[i].value+">"+data[i].text+"</option>";
						menuitem_select.append(option);
					}
				}
			}
		});
	});

		//inital link input and category select based on the update page and create page

	$(".field-category").css("display","none");
	$('#id_link').attr('readonly','readonly');
	$(".field-link").css("display","none");
	
	if ($('#id_name').val().length > 0){
		if ($('#id_link_type').val() == 'category'){
			$(".field-category").css("display","table-header-group");
			$(".field-link").css("display","none")
			$('#id_link').attr('value','http://'+window.location.hostname+'/#');
		}
		else if ($('#id_link_type').val() == 'link'){
			$('#id_link').removeAttr('readonly');
			$(".field-link").css("display","table-header-group")
		}
		else if ($('#id_link_type').val() == 'news'){
			$(".field-link").css("display","table-header-group")
		}
	}


	//initial link_type select

	$('#id_link_type').change(function(){
		if ($(this).val() == 'news'){
			$(".field-link").css("display","table-header-group")
			$('#id_link').attr('readonly','readonly');
			$('#id_link').attr('value','http://'+window.location.hostname+'/news/');
			$(".field-category").css("display","none");
			$('#id_category').attr('value','');
		}
		else if ($(this).val() == 'category'){
			$(".field-link").css("display","none");
			$('#id_link').attr('value','http://'+window.location.hostname+'/#');
			$(".field-category").css("display","table-header-group");
		}
		else {
			$(".field-link").css("display","table-header-group")
			$('#id_link').removeAttr('readonly');
			$('#id_link').attr('value','');
			$(".field-category").css("display","none");
			$('#id_category').attr('value','');
		}
	});
});