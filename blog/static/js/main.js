$(document).ready(function() {

    //AJAX GET
    $.ajax({
        type:"GET",
        url: "/ajax/more",
        success: function(data) {
            for(i=0;i<data.length;i++){
                $('ul').append('<li>'+data[i]+'</li>');
            }
        }
    });

});