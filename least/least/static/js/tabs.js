var tab_content;
var tabs;
var line_title;
var underLine;
var par_title;
var tab_list=[];
window.onload = function(){
	
	tab_content = document.getElementsByClassName('sections');
	tabs = document.getElementsByClassName('tab');
	line_title = document.getElementsByClassName('test_title');
	par_title = document.getElementsByClassName('test_par');
	underLine = document.getElementsByClassName('under_line');
	var fiveMinutes = 60 * 30,
		       display = document.querySelector('#time');
	startTimer(fiveMinutes, display);
	CloseTab();
	tab_content[0].style.display = 'block';
	tabs[0].classList.add('active');
	underLine[0].style.display = 'block';
	tab_list.push(0)
}

function CloseTab(){
	for(var i = 0; i < tab_content.length; i++){
		tab_content[i].style.display = 'none';
		tabs[i].classList.remove('active');
		underLine[i].style.display = "none";
	}
}

// document.getElementById('tab-wrapper').onclick = function(target){
// 	var target = event.target;
// 	for(var i = 0; i < 6; i++){
// 		if(target == tabs[i]){
// 			if(!tab_list.includes(i)){
// 				CloseTab();
// 				alert("Do you want leave?")
// 				tab_content[i].style.display = 'block';
// 				target.classList.add('active');
// 				line_title[0].innerHTML = tabs[i].innerHTML;
// 				underLine[i].style.display = 'block'; 
// 				tab_list.push(i);
// 				console.log(tab_list+" kmkmkx")
// 				break;
// 			}
// 		}
// 	}
// }
function startTimer(duration, display) {
	    var timer = duration, minutes, seconds;
	    setInterval(function () {
	        minutes = parseInt(timer / 60, 10)
	        seconds = parseInt(timer % 60, 10);

	        minutes = minutes < 10 ? "0" + minutes : minutes;
	        seconds = seconds < 10 ? "0" + seconds : seconds;

	        display.textContent = minutes + ":" + seconds;

	        if (--timer < 0) {
	            document.getElementById("return_statment").click()
	        }
	    }, 1000);
	}
var modal = document.getElementById('myModal');

var modal_end = document.getElementById('endModal');
// When the user clicks the button, open the modal 
$('#myBtn').click(function(){
	modal.style.display = "block";
});
$('#myBtnCancer').click(function(){
    modal.style.display = "none";
});

window.onclick = function(event) {
    if (event.target == modal) {
       modal.style.display = "none";
    }
}
$('#btnEnd').click(function(){

	var i =tab_list.pop()+1;
	tab_list.push(i-1);
	if(!tab_list.includes(i)){
		console.log(tab_list);
		CloseTab();
		tab_content[i].style.display = 'block';
		tabs[i].classList.add('active');
		line_title[0].innerHTML = tabs[i].innerHTML;
		underLine[i].style.display = 'block'; 

		tab_list.push(i);
		modal.style.display="none";
		if (i==4) {
			document.getElementById("myBtn").style.display="none";
			document.getElementById("endbtn").style.display="block"
		}
	}
});
$('#endbtn').click(function(){
	modal_end.style.display = "block";
});
$('#BtnCancer').click(function(){
    modal_end.style.display = "none";
    });
