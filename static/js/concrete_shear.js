$(document).ready(function(){
    $('#structure_type').on('change', function(){
        val = $("#structure_type").val()
        if (val == 2)
            $("#slab_thickness").attr("disabled",false);
        else
            $("#slab_thickness").attr("disabled",true);
    });
    $("#structure_type").trigger("change")
});
