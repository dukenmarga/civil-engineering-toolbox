$(document).ready(function(){
    $(".table").tablesorter();
    $("table").floatThead({ useAbsolutePositioning: false, zIndex: 1 });
    $("thead").css('background-color', '#fff')
});