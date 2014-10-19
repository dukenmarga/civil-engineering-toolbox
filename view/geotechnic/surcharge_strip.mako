<%inherit file="../base.mako"/>

<%block name="content">
    <h4>Strip Load</h4>
    <div class="row">
        <div class="col-md-6">
            <form role="form" action="/geotechnic/surcharge/strip-load" method="get">
                <div class="row">
                    <div class="col-md-6">
                        <label for="q">Strip Load (Q)</label>
                     </div>
                    <div class="col-md-6">
                        <input type="text" name="q" id="q" value="${q}"> KN/m2
                    </div>
                </div>
                <div class="row">
                    <div class="col-md-6">
                        <label for="x_load">Distance from edge (x)</label>
                    </div>
                    <div class="col-md-6">
                        <input type="text" name="x_load" id="x_load" value="${x_load}"> m
                    </div>
                </div>
                <div class="row">
                    <div class="col-md-6">
                        <label for="width">Width Load (B)</label>
                    </div>
                    <div class="col-md-6">
                        <input type="text" name="width" id="width" value="${width}"> m
                    </div>
                </div>
                <div class="row">
                    <div class="col-md-6">
                        <label for="H">Depth (H)</label>
                    </div>
                    <div class="col-md-6">
                        <input type="text" name="H" id="H" value="${H}"> m
                    </div>
                </div>
                <div class="row">
                    <div class="col-md-6">
                        <label for="start">Left Boundary</label>
                    </div>
                    <div class="col-md-6">
                        <input type="text" name="start" id="start" value="${start}"> m
                    </div>
                </div>
                <div class="row">
                    <div class="col-md-6">
                        <label for="end">Right Boundary</label>
                    </div>
                    <div class="col-md-6">
                        <input type="text" name="end" id="end" value="${end}"> m
                    </div>
                </div>
                <hr>
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