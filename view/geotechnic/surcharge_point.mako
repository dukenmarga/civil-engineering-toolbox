<%inherit file="../base.mako"/>

<%block name="content">
    <h4>Point Load</h4>
    <div class="row">
        <div class="col-md-6">
            <form role="form" action="/geotechnic/surcharge/point-load" method="get">
                ${row("q", q, "Point Load (Q)", "KN")}
                ${row("x_load", x_load, "Distance from edge (x)", "m")}
                ${row("H", H, "Depth (H)", "m")}
                ${row("start", start, "Left Boundary", "m")}
                ${row("end", end, "Right Boundary", "m")}
                <div class="row">
                    <div class="col-md-6">
                        <input type="submit" class="btn btn-primary" value="Analyze"><br>
                    </div>
                </div>
            </form>
            <hr>
            <h4>Doc</h4>
            ${doc}
        </div>
        <div id='plot' class="col-md-6">
            <img src="data:image/png;base64,${plot_image}" width="640" height="480" border="0" />
        </div>
    </div>
</%block>

<%block name="css">
</%block>

<%block name="javascript">
</%block>

<%def name="row(name, val, title, unit)">
    <div class="row">
        <div class="col-md-6">
            <label for="${name}">${title}</label>
         </div>
        <div class="col-md-6">
            <input type="text" name="${name}" id="${name}" value="${val}"> ${unit}
        </div>
    </div>
</%def>