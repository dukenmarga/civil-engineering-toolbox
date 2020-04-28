<%inherit file="../base.mako"/>

<%block name="content">
    <h4>Strip Load</h4>
    <div class="row">
        <div class="col-md-6">
            <form role="form" action="/geotechnic/surcharge/strip-load" method="get">
                ${row("q", q, "Strip Load (Q)", "KN/m2")}
                ${row("x_load", x_load, "Distance from edge (x)", "m")}
                ${row("width", width, "Width Load (B)", "m")}
                ${row("H", H, "Depth (H)", "m")}
                ${row("start", start, "Left Boundary", "m")}
                ${row("end", end, "Right Boundary", "m")}
                ${row("type", type, "Type of Retaining Wall", "<br><i>1:Flexible 2:Rigid</i>")}
                <div class="row">
                    <div class="col-md-6">
                        <input type="submit" class="btn btn-primary" value="Analyze"><br>
                    </div>
                </div>
            </form>
        </div>
        <div id='plot' class="col-md-6">
            <img src="data:image/png;base64,${plot_image.decode('utf8')}" width="640" height="480" border="0" />
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
