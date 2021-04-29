function open_close_all_fail(name) {
	var s = "details_failure_" + name
	var elem = document.getElementsByClassName(s)[0]
	var test = elem.getElementsByTagName("details")
	if (elem.open == true) {
		elem.open = false;
		document.getElementById("btn_failure_" + name).textContent = "Unfold"
		for (var i = 0; i < test.length; i++) {
		    test[i].open = false;
		}
	} else {
		elem.open = true;
		document.getElementById("btn_failure_" + name).textContent = "Fold"
		for (var i = 0; i < test.length; i++) {
		    test[i].open = true;
		}
	}
}

function open_close_all_success(name) {
	var s = "details_success_" + name
	var elem = document.getElementsByClassName(s)[0]
	var test = elem.getElementsByTagName("details")
	if (elem.open == true) {
		elem.open = false;
		document.getElementById("btn_success_" + name).textContent = "Unfold"
		for (var i = 0; i < test.length; i++) {
		    test[i].open = false;
		}
	} else {
		elem.open = true;
		document.getElementById("btn_success_" + name).textContent = "Fold"
		for (var i = 0; i < test.length; i++) {
		    test[i].open = true;
		}
	}
}

function open_close_all_warning(name) {
	var s = "details_warning_" + name
	var elem = document.getElementsByClassName(s)[0]
	var test = elem.getElementsByTagName("details")
	if (elem.open == true) {
		elem.open = false;
		document.getElementById("btn_warning_" + name).textContent = "Unfold"
		for (var i = 0; i < test.length; i++) {
		    test[i].open = false;
		}
	} else {
		elem.open = true;
		document.getElementById("btn_warning_" + name).textContent = "Fold"
		for (var i = 0; i < test.length; i++) {
		    test[i].open = true;
		}
	}
}

function scrollToTop() {
	window.scrollTo({ top: 0, behavior: 'smooth' });
}
