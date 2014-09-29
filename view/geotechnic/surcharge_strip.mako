<%inherit file="../base.mako"/>

<%block name="content">
    <h4>Point Load</h4>
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
    <script>
    $(document).ready(function(){
        /* Plot 3D Surcharge Load */
        var data = null;
        var graph = null;

        // Called when the Visualization API is loaded.
        function drawVisualization() {
            // create some shortcuts to math functions
            var sqrt = Math.sqrt;
            var pow = Math.pow;
            var sin = Math.sin;
            var cos = Math.cos;
            var atan = Math.atan;
            var pi = Math.PI;

            var q = ${q}; //KN
            var x_load = ${x_load}; //m
            var width = ${width}; //m
            var H = ${H}; //m
            m = x_load/H;

            // create the data table.
            data = new vis.DataSet();

            // create the animation data
            var start = ${start}; //m
            var end = ${end}; // m
            delta1 = (end-start)/100;
            delta2 = H/100;

            // x=i=length; z=j=depth;
            for (var i=start; i<end; i+=delta1) {
                for (var j=0.01; j<H; j+=delta2){
                    var x = i;
                    var alpha = atan((x_load+width/2)/j); //rad
                    var gamma = atan((x_load+width)/j); //rad
                    var beta = (gamma-alpha)*2; //rad

                    var y = 2*q/pi*( (beta+sin(beta))*pow(sin(alpha),2) + (beta-sin(alpha))*pow(cos(alpha),2) );
                    var z = -j;

                    data.add({x:x,y:-y,z:z,style:y});
                }
            }

            // specify options
            var options = {
                width:  '500px',
                height: '500px',
                style: 'dot-color',
                showPerspective: true,
                showGrid: true,
                keepAspectRatio: true,
                verticalRatio: 1.0,
                legendLabel: 'Pressure (KN/m2)',
                xLabel: 'Distance (m)',
                yLabel: 'Pressure (KN/m2)',
                zLabel: 'Depth (m)',
                cameraPosition: {
                    horizontal: -0.35,
                    vertical: 0.22,
                    distance: 1.8
                    }
            };

            // create our graph
            var container = document.getElementById('plot');
            graph = new vis.Graph3d(container, data, options);
        }
        drawVisualization()
    });
    </script>
</%block>