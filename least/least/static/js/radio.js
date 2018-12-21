$(document).ready(function(){
    $('.category').bind('click', function() {
        var check = true;
        $("input:radio").each(function(){
            var name = $(this).attr("name");
            if($("input:radio[name="+name+"]:checked").length == 0){
                check = false;
            }
        });
      	var return_statment=document.getElementById('return_statment')
        if(check){
            return_statment.style.display='block';
        }else{
        	return_statment.style.display='none';
        }
    });
});
    $('#return_statment').click(function(){
    	list=[];
        alert('clicked')
    	var rates = document.getElementsByClassName('button_radio');
		$("input:radio").each(function(){
            alert('checking')
            var name = $(this).attr("name");
            if($("input:radio[name="+name+"]:checked")){
              	var radioValue = $("input[name="+name+"]:checked").val();
                list.push(name);
            	list.push(radioValue);
        	}
            else{
                list.push(name);
                list.push(0);
            }
        	var myform = document.createElement('form');
			var product = document.createElement('input');
			product.value = list;
			product.name = "res";
			myform.action = "result/";
			myform.method = "get";
			myform.appendChild(product);
			document.body.appendChild(myform);
			myform.submit();
    	});
		});
