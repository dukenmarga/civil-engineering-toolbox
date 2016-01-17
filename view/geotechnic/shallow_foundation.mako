<%inherit file="../base.mako"/>

<%block name="content">
    <h4>Shallow Foundation Analysis</h4>
    <div class="row">
        <div class="col-md-6">
            <form role="form" action="/geotechnic/shallow-foundation/analysis" method="get">
                ${text("width", width, "Width (B)", "m")}
                ${text("length", length, "Length (L)", "m")}
                ${text("thick", thick, "Footing Thickness (t)", "m")}
                ${text("height", height, "Height of Foundation (h)", "m")}
                ${text("Hx", Hx, "Horizontal Load X", "kg")}
                ${text("Hy", Hy, "Horizontal Load Y", "kg")}
                ${text("V", V, "Vertical Load", "kg")}
                ${text("qall", qall, "Q allowable soil", "kg/m2")}
                ${text("friction", friction, "Foundation-Soil Friction", "")}
                ${text("conc_unit_weight", conc_unit_weight, "Conc. Unit Weight", "kg/m3")}
                <div class="row">
                    <div class="col-md-6">
                        <input type="submit" class="btn btn-primary" value="Analyze"><br>
                    </div>
                </div>
            </form>
        </div>
        <div id='result' class="col-md-6">
            Q<sub>1</sub> = ${q1} kg/m2<br>
            Q<sub>2</sub> = ${q2} kg/m2<br>
            Q<sub>3</sub> = ${q3} kg/m2<br>
            Q<sub>max</sub> = ${qmax} kg/m2<br>
            Q<sub>min</sub> = ${qmin} kg/m2<br>
            Status for Q<sub>max</sub> = ${status_max} <br>
            Status for Q<sub>min</sub> = ${status_min} <br>
            SF Sliding X = ${SF_slide_x} <br>
            SF Sliding Y = ${SF_slide_y} <br>
            SF Overturning X = ${SF_overturn_x} <br>
            SF Overturning Y = ${SF_overturn_y} <br>
        </div>
    </div>
</%block>

<%block name="css">
</%block>

<%block name="javascript">
</%block>

<%def name="text(name, val, title, unit)">
    <div class="row">
        <div class="col-md-6">
            <label for="${name}">${title}</label>
         </div>
        <div class="col-md-6">
            <input type="text" name="${name}" id="${name}" value="${val}"> ${unit}
        </div>
    </div>
</%def>