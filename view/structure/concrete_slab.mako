<%inherit file="../base.mako"/>

<%block name="content">
    <h4>Slab Reinforcement</h4>
    <div class="row">
        <div class="col-md-6">
            <form role="form" action="/structure/concrete/slab-two-ways" method="get">
                ${row("ly", ly, "Long span (ly)", "m")}
                ${row("lx", lx, "Short span (lx)", "m")}
                ${row("t", t, "Slab Thickness (t)", "m")}
                ${row("dl", dl, "Dead Load (DL)", "kg/m2")}
                ${row("ll", ll, "Live Load (LL)", "kg/m2")}
                ${row("kdl", kdl, "k*DL", "")}
                ${row("kll", kll, "k*LL", "")}
                ${row("conc_unit_weight", conc_unit_weight, "Concrete Mass Weight", "kg/m3")}
                ${row("fc", fc, "Concrete Strength, $f_c'$", "MPa")}
                ${row("fus", fus, "Steel Strength, $f_{us}$", "MPa")}
                ${select("slab_type", slab_type, "Slab Type", "")}
                ${row("diameter", diameter, "Reinforcement Diameter", "mm")}
                ${row("dy", dy, "dy", "mm")}
                ${row("dx", dx, "dx", "mm")}
                <div class="row">
                    <div class="col-md-6">
                        <input type="submit" class="btn btn-primary" value="Analyze"><br>
                    </div>
                </div>
            </form>
        </div>
        <div id='plot' class="col-md-6">
            <span class="label label-danger">Important</span> This program is not completed yet.<br>
            Mlx = ${Mlx/1e6} KNm, <strong>${diameter} @ ${slx}</strong><br>
            Mly = ${Mly/1e6} KNm, <strong>${diameter} @ ${sly}</strong><br>
            Mtx = ${Mtx/1e6} KNm, <strong>${diameter} @ ${stx}</strong><br>
            Mty = ${Mty/1e6} KNm, <strong>${diameter} @ ${sty}</strong><br>
            <span class="label label-danger">${error}</span><br>
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
<%def name="select(name, val, title, unit)">
    <div class="row">
        <div class="col-md-6">
            <label for="${name}">${title}</label>
         </div>
        <div class="col-md-6">
            <select id="${name}" name="${name}" class="form-control">
                ${option(val, '1', "1 (None of the edges is fixed)")}
                ${option(val, '2', "2 (All of four the edges are fixed)")}
                ${option(val, '3', "3 (Only two adjacent edges is free)")}
                ${option(val, '4', "4 (The two long edges are free)")}
                ${option(val, '5', "5 (The two short edges are free)")}
                ${option(val, '6', "6 (Only one short edge is fixed)")}
                ${option(val, '7', "7 (Only one long edge is fixed)")}
                ${option(val, '8', "8 (Only one long edge is free)")}
                ${option(val, '9', "9 (Only one short edge is free)")}
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