$(document).ready(function(){
    // Pressure Converter
    $('#pressureFromNumber').on('keyup', function(){
            pressureConvert();
    });
    $('#pressureFromUnit, #pressureToUnit').on('change', function(){
            pressureConvert();
    });
    function pressureConvert(){
        val = $("#pressureFromNumber").val()
        from = $("#pressureFromUnit").val()
        to = $("#pressureToUnit").val()
        $.ajax({
            type: 'GET',
            url: "/math/unit_converter/pressure/",
            data: { val: val, from_: from, to: to }
        }).done(function(r) {
            $("#pressureToNumber").text(r);
        });
    }

    // Force Converter
    $('#forceFromNumber').on('keyup', function(){
            forceConvert();
    });
    $('#forceFromUnit, #forceToUnit').on('change', function(){
            forceConvert();
    });
    function forceConvert(){
        val = $("#forceFromNumber").val()
        from = $("#forceFromUnit").val()
        to = $("#forceToUnit").val()
        $.ajax({
            type: 'GET',
            url: "/math/unit_converter/force/",
            data: { val: val, from_: from, to: to }
        }).done(function(r) {
            $("#forceToNumber").text(r);
        });
    }

    // Distance Converter
    $('#distanceFromNumber').on('keyup', function(){
            distanceConvert();
    });
    $('#distanceFromUnit, #distanceToUnit').on('change', function(){
            distanceConvert();
    });
    function distanceConvert(){
        val = $("#distanceFromNumber").val()
        from = $("#distanceFromUnit").val()
        to = $("#distanceToUnit").val()
        $.ajax({
            type: 'GET',
            url: "/math/unit_converter/distance/",
            data: { val: val, from_: from, to: to }
        }).done(function(r) {
            $("#distanceToNumber").text(r);
        });
    }
});
