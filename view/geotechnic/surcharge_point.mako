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
            <!-- SurfacePlot goes here... -->
        </div>
    </div>
</%block>

<%block name="css">
    <link href="/static/vis/dist/vis.min.css"
        rel="stylesheet" type="text/css" />
</%block>

<%block name="javascript">
    <script src="/static/vis/dist/vis.min.js"></script>
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
            var cos = Math.cos;
            var atan = Math.atan;

            var q = ${q}; //KN
            var x_load = ${x_load}; //m
            var H = ${H}; //m
            m = x_load/H;
            if(m>0.4){
                A = 1.77;
                B = pow(m,2);
                C = B;
            } else {
                A = 0.28;
                B = 0.16;
                C = 1;
            }

            // create the data table.
            data = new vis.DataSet();

            // create the animation data
            var start = ${start}; //m
            var end = ${end}; // m
            delta = (end-start)/100;
            for (var i=start; i<end; i+=delta) {
                for (var j=0; j<H; j+=0.2){
                    var n = j/H;
                    var x = i;
                    n2 = pow(n,2)
                    var y = A*q/pow(H,2)*C*n2/pow(B+n2,3);
                    pi = atan((i/x_load));//rad
                    var y1 = -y*pow(cos(1.1*pi),2)
                    var z = -j;

                    data.add({x:x,y:y1,z:z,style:y1});
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