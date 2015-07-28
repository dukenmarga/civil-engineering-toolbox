<%inherit file="../base.mako"/>

<%block name="content">
    <h4>Response Spectrum</h4>
    <div class="row">
        <div class="col-md-6">
            <form role="form" action="/structure/earthquake/response-spectrum" method="get">
                ${row("ss", ss, "Ss", "")}
                ${row("s1", s1, "S1", "")}
                ${option("site_class", site_class, "Site Class", "")}
                ${row("design_coefficient", design_coefficient,
                "Design Coefficient ($S_{DS},S_{D1}$)",
                "$\\times\\space S_{MS},S_{M1}$")}
                <div class="row">
                    <div class="col-md-6">
                        <input type="submit" class="btn btn-primary" value="Analyze"><br>
                    </div>
                </div>
            </form>
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
<%def name="option(name, val, title, unit)">
    <div class="row">
        <div class="col-md-6">
            <label for="${name}">${title}</label>
         </div>
        <div class="col-md-6">
            <select id="${name}" name="${name}" class="form-control">
                % if site_class=="SA":
                    <option value="SA" selected="selected">SA (Hard rock)</option>
                % else:
                    <option value="SA">SA (Hard rock)</option>
                % endif

                % if site_class=="SB":
                    <option value="SB" selected="selected">SB (Rock)</option>
                % else:
                    <option value="SB">SB (Rock)</option>
                % endif

                % if site_class=="SC":
                    <option value="SC" selected="selected">SC (Very dense soil and soft rock)</option>
                % else:
                    <option value="SC">SC (Very dense soil and soft rock)</option>
                % endif

                % if site_class=="SD":
                    <option value="SD" selected="selected">SD (Stiff soil)</option>
                % else:
                    <option value="SD">SD (Stiff soil)</option>
                % endif
                % if site_class=="SE":
                    <option value="SE" selected="selected">SE (Soft clay soil)</option>
                % else:
                    <option value="SE">SE (Soft clay soil)</option>
                % endif
            </select>
        </div>
    </div>
</%def>