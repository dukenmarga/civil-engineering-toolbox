<%inherit file="../base.mako"/>

<%block name="content">
    <h4>Concrete Two-Way Shear Design</h4>
    <div class="row">
        <div class="col-md-6">
            <form role="form" action="/structure/concrete/twoway-shear-design" method="get">
                ${text("fc", fc, "Concrete strength, $f_c'$", "MPa")}
                ${text("fyr", fyr, "Reinf.yield strength ($f_{yr}$)", "MPa")}
                ${select_concrete("concrete_type", concrete_type, "Concrete", "")}
                ${select_column("column_type", column_type, "Column", "")}
                ${text("thickness", thickness, "Thickness", "mm")}
                ${text("perimeter", perimeter, "Perimeter (bo)", "mm")}
                ${text("width", width, "Width (b)", "mm")}
                ${text("Length", length, "Length (l)", "mm")}
                ${text("diameter", diameter, "Diameter (D)", "mm")}
                ${text("cover", cover, "Cover", "mm")}
                ${text("Vu", Vu, "Vu", "N")}
                <div class="row">
                    <div class="col-md-6">
                        <input type="submit" class="btn btn-primary" value="Analyze"><br>
                    </div>
                </div>
            </form>
        </div>
        <div id='plot' class="col-md-6">
            Vc = ${Vc} N<br>
            $\phi$ = ${phi}<br>
            $\phi$Vc = ${phi*Vc} N<br>
        </div>
    </div>
</%block>

<%block name="css">
</%block>

<%block name="javascript">
    <script src="/static/js/concrete_shear.js"></script>
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

<%def name="select_concrete(name, val, title, unit)">
    <div class="row">
        <div class="col-md-6">
            <label for="${name}">${title}</label>
         </div>
        <div class="col-md-6">
            <select id="${name}" name="${name}" class="">
                ${option(val, 1, "Normal Concrete")}
                ${option(val, 0.85, "Sand-lightweight Concrete")}
                ${option(val, 0.75, "All Lightweight Concrete")}
            </select>
        </div>
    </div>
</%def>

<%def name="select_column(name, val, title, unit)">
    <div class="row">
        <div class="col-md-6">
            <label for="${name}">${title}</label>
         </div>
        <div class="col-md-6">
            <select id="${name}" name="${name}" class="">
                ${option(val, 40, "Interior Column")}
                ${option(val, 30, "Edge column")}
                ${option(val, 20, "Corner column")}
            </select>
        </div>
    </div>
</%def>

<%def name="option(val, no, text)">
    % if val==no:
        <option value="${no}" selected="selected">${text}</option>
    % else:
        <option value="${no}">${text}</option>
    % endif
</%def>