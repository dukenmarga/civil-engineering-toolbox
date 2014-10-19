<%inherit file="../base.mako"/>

<%block name="content">
    <h4>Point Load</h4>
    <div class="row">
        <div class="col-md-6">
            <form role="form" action="/geotechnic/surcharge/point-load" method="get">
                <div class="row">
                    <div class="col-md-6">
                        <label for="q">Point Load (Q)</label>
                     </div>
                    <div class="col-md-6">
                        <input type="text" name="q" id="q" value="${q}"> KN
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
            <!-- SurfacePlot goes here... -->
        </div>
    </div>
</%block>

<%block name="css">
    <link href="/static/vis/src/vis.min.css"
        rel="stylesheet" type="text/css" />
</%block>

<%block name="javascript">
    <script src="/static/vis/src/vis.min.js"></script>

</%block>