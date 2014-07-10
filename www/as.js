function Checkall(form,type){ 
	name="package_"+type+"[]";
	for (var i = 1; i < form.elements.length; i++){    
		if (form.elements[i].name==name) {
			form.elements[i].checked=form.elements[name][0].checked;
		}
	} 
}

/*
function as_search_hide() {
	document.getElementById("as_search_hide").style.className="as_hidden";
	document.getElementById("as_search_show").style.className="as_visible";
}
function as_search_show() {
	document.getElementById("as_search_hide").style.className="as_visible";
	document.getElementById("as_search_show").style.className="as_hidden";
}*/

/*
function as_search(form) {
	form.submit();
}

function as_show_all(form) {
	form.elements["filter"].value="";
	form.submit();
}
*/