<%inherit file="../base.mako"/>

<%block name="content">
    <h4>Options</h4>
    <div class="alert alert-info" role="alert">
    This page is intended to store preferred options value that will
        fill your input form. This value will be applied only for your own browser.
        You can override this value in input form each time you use different
        application.
    </div>
    <form role="form" action="options/save" method="get">
        <div class="row col-md-6">
        <h4>Reinforced Concrete</h4>
            ${text("fc", "Compressive Strength (fc)", fc.value, "MPa")}
            ${text("fyr", "Reinforcement Tensile Strength (fyr)", fyr.value, "MPa")}
            ${text("Ec", "Young Modulus (Ec)", Ec.value, "MPa")}
            ${text("conc_unit_weight", "Concrete Unit Weight", conc_unit_weight.value, "kg/m3")}
            ${text("conc_poisson_ratio", "Possion's Ratio", conc_poisson_ratio.value, "")}
        <hr>
        <h4>Steel</h4>
            ${text("fys", "Yield Tensile Strength (fys)", fys.value, "MPa")}
            ${text("fus", "Ultimate Tensile Strength (fus)", fus.value, "MPa")}
            ${text("Es", "Young Modulus (Es)", Es.value, "MPa")}
            ${text("steel_unit_weight", "Steel Unit Weight", steel_unit_weight.value, "kg/m3")}
            ${text("steel_poisson_ratio", "Possion's Ratio", steel_poisson_ratio.value, "")}
            <hr>
        </div>
        <div class="row col-md-6">
            <div class="row">
                <input type="submit" class="btn btn-primary" value="Save"><br>
                <hr>
                <strong><a href="/options/reset" class="confirm"
                        q="Do you want to reset to default options? This operation can't be undone.">
                    Reset options to defaults</a></strong>
            </div>
        </div>
    </form>
</%block>

<%def name="text(id, description, val, unit)">
    <div class="row">
        <div class="col-md-6">
            ${description}
         </div>
        <div class="col-md-6">
            <input type="text" name="${id}" id="${id}" value="${val}"> ${unit}
        </div>
    </div>
</%def>