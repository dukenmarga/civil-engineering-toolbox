<%inherit file="../base.mako"/>

<%block name="content">
    <h4>Options</h4>
    <p>This page is intended to store preferred options value that will
        fill your input form. This value will be applied only for your own browser.
        You can override this value in input form each time you use different
        application.
    </p>
    <form role="form" action="options/save" method="get">
        <div class="row col-md-6">
        <h4>Reinforced Concrete Structure</h4>
            <div class="row">
                <div class="col-md-6">
                    <label for="fc">Compressive Strength (fc')</label>
                 </div>
                <div class="col-md-6">
                    <input type="text" name="fc" id="fc" value="${fc.value}"> MPa
                </div>
            </div>
            <div class="row">
                <div class="col-md-6">
                    <label for="Gc">Shear Modulus (Gc)</label>
                </div>
                <div class="col-md-6">
                    <input type="text" name="Gc" id="Gc" value="${Gc.value}"> MPa
                </div>
            </div>
            <div class="row">
                <div class="col-md-6">
                    <label for="fyr">Reinforcement Tensile Strength (fyr)</label>
                </div>
                <div class="col-md-6">
                    <input type="text" name="fyr" id="fyr" value="${fyr.value}"> MPa
                </div>
            </div>
            <div class="row">
                <div class="col-md-6">
                    <label for="conc_unit_weight">Concrete Unit Weight</label>
                </div>
                <div class="col-md-6">
                    <input type="text" name="conc_unit_weight" id="conc_unit_weight" value="${conc_unit_weight.value}"> kg/m3
                </div>
            </div>
        <hr>
        <strong><i>Steel Structure</i></strong>
            <div class="row">
                <div class="col-md-6">
                    <label for="fys">Yield Tensile Strength (fys)</label>
                </div>
                <div class="col-md-6">
                    <input type="text" name="fys" id="fys" value="${fys.value}"> MPa
                </div>
            </div>
            <div class="row">
                <div class="col-md-6">
                    <label for="fus">Ultimate Tensile Strength (fus)</label>
                </div>
                <div class="col-md-6">
                    <input type="text" name="fus" id="fus" value="${fus.value}"> MPa
                </div>
            </div>
            <div class="row">
                <div class="col-md-6">
                    <label for="steel_unit_weight">Steel Unit Weight</label>
                </div>
                <div class="col-md-6">
                    <input type="text" name="steel_unit_weight" id="steel_unit_weight" value="${steel_unit_weight.value}"> kg/m3
                </div>
            </div>
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