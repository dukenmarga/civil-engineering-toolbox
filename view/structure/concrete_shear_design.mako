<%inherit file="../base.mako"/>

<%block name="content">
    <h4>Concrete Shear Design</h4>
    <div class="row">
        <div class="col-md-6">
            <form role="form" action="/structure/concrete/shear-design" method="get">
                ${text("fc", fc, "Concrete strength, $f_c'$", "MPa")}
                ${select("concrete_type", concrete_type, "Concrete", "")}
                ${text("fyr", fyr, "Reinf.yield strength ($f_{yr}$)", "MPa")}
                ${text("height", height, "Height (h)", "mm")}
                ${text("width", width, "Width (b)", "mm")}
                ${text("diameter", diameter, "Diameter (D)", "mm")}
                ${text("cover", cover, "Cover", "mm")}
                ${text("leg", leg, "Leg", "")}
                ${text("Vu", Vu, "Vu", "N")}
                ${text("P", P, "Axial (+compression, -tension)", "N")}
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
            Zone = <strong>${zone}</strong><br>
            Use <strong>Dia ${diameter} @ ${space}</strong> mm<br>
            Vs = ${Vs} N<br>
            $\phi$(Vs+Vc) = ${phi*(Vs+Vc)} N<br>
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

<%def name="select(name, val, title, unit)">
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

<%def name="option(val, no, text)">
    % if val==no:
        <option value="${no}" selected="selected">${text}</option>
    % else:
        <option value="${no}">${text}</option>
    % endif
</%def>