<%inherit file="../base.mako"/>

<%block name="javascript">
    <script src="/static/js/converter.js"></script>
</%block>

<%block name="content">
    <ul class="nav nav-tabs" id="converter" role="tablist">
        <li class="active" ><a href="#pressure" role="tab" data-toggle="tab">
            Pressure</a></li>
        <li><a href="#force" role="tab" data-toggle="tab">Force</a></li>
        <li><a href="#distance" role="tab" data-toggle="tab">Distance</a></li>
    </ul>
    <div id="converterContent" class="tab-content col-md-6 col-md-offset-3">
        ${section("pressure", "Pressure Converter", "pressureFromNumber",
                "pressureToNumber", "pressureFromUnit", "pressureToUnit",
                pressure, "active")}
        ${section("force", "Force Converter", "forceFromNumber",
                "forceToNumber", "forceFromUnit", "forceToUnit",
                force, "")}
        ${section("distance", "Distance Converter", "distanceFromNumber",
                "distanceToNumber", "distanceFromUnit", "distanceToUnit",
                distance, "")}
    </div>
    <script>
        $('#converter a').click(function (e) {
            e.preventDefault()
            $(this).tab('show')
        })
    </script>
</%block>

<%def name="section(name, title, idFromNumber, idToNumber, idFromUnit, idToUnit,
                    unit_list, clss)">
    <div id="${name}" class="tab-pane ${clss}">
        <h4>${title}</h4>
        <form role="form">
            <div class="row">
                <div class="col-md-6">
                    From
                </div>
                <div class="col-md-6">
                    To
                </div>
            </div>
            <div class="row">
                <div class="col-md-6">
                    <input value="1" type="text" id="${idFromNumber}">
                </div>
                <div class="col-md-6">
                    <span id="${idToNumber}">1</span>
                </div>
            </div>
            <div class="row">
                <div class="col-md-6">
                    <select class="form-control" id="${idFromUnit}" size="15">
                        ${unit_list}
                    </select>
                </div>
                <div class="col-md-6">
                    <select class="form-control" id="${idToUnit}" size="15">
                        ${unit_list}
                    </select>
                </div>
            </div>
        </form>
    </div>
</%def>