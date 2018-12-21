    // $(document).ready(function(){
    //     $('input[type="radio"]').click(function(){
    //         if($(this).prop("checked") == true || ){
    //             alert("Checkbox is checked.");
    //         }
    //         else if($(this).prop("checked") == false){
    //             alert("Checkbox is unchecked.");
    //         }
    //     });
    // });
$('input[type="radio"]').change(function(){
    if ($('.input[type="radio"]:checked').length == $('.input[type="radio"]').length) {
       var result=document.getElementByClassName('result');
       result.style.display = 'block';
    }
});