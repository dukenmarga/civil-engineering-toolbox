<%inherit file="../base.mako"/>

<%block name="content">
    <h4>Concrete One-Way Shear Design</h4>
    <div class="row">
        <div class="col-md-6">
            <form role="form" action="/structure/concrete/oneway-shear-design" method="get">
                ${text("fc", fc, "Concrete strength, $f_c'$", "MPa")}
                ${select_concrete("concrete_type", concrete_type, "Concrete", "")}
                ${select_structure("structure_type", structure_type, "Type", "")}
                ${text("slab_thickness", slab_thickness, "Flange Thickness", "mm")}
                ${text("fyr", fyr, "Reinf.yield strength ($f_{yr}$)", "MPa")}
                ${text("height", height, "Height (h)", "mm")}
                ${text("width", width, "Width (b) or Perimeter (bo)", "mm")}
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

<%def name="select_structure(name, val, title, unit)">
    <div class="row">
        <div class="col-md-6">
            <label for="${name}">${title}</label>
         </div>
        <div class="col-md-6">
            <select id="${name}" name="${name}" class="">
                ${option(val, 1, "Beam")}
                ${option(val, 2, "Beam Integral With Slab")}
                ${option(val, 3, "Slab or Footing")}
                ${option(val, 4, "One-Way Joist System")}
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