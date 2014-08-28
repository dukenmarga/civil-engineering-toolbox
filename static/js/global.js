$(document).ready(function(){
    /* Table fixed header */
    $(".table").tablesorter();
    $("table").floatThead({ useAbsolutePositioning: false, zIndex: 1 });
    $("thead").css('background-color', '#fff')

    /* Confirmation */
    $('.confirm').click(function(){
        var q = $(this).attr('q');
        var ans = confirm(q);
        if(ans){
            return true;
        } else {
            return false;
        }
    });

});