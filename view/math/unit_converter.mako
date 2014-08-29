<%inherit file="../base.mako"/>

<%block name="javascript">
    <script src="/static/js/converter.js"></script>
</%block>

<%block name="content">
    <ul class="nav nav-tabs" id="converter" role="tablist">
        <li class="active" ><a href="#pressure" role="tab" data-toggle="tab">
            Pressure</a></li>
        <li><a href="#force" role="tab" data-toggle="tab">Force</a></li>
        <li><a href="#distance" role="tab" data-toggle="tab">Distance</a></li>
    </ul>
    <div id="converterContent" class="tab-content col-md-6 col-md-offset-3">
        <div id="pressure" class="tab-pane active">
            <h4>Pressure Converter</h4>
            <form role="form">
                <div class="row">
                    <div class="col-md-6">
                        From
                    </div>
                    <div class="col-md-6">
                        To
                    </div>
                </div>
                <div class="row">
                    <div class="col-md-6">
                        <input value="1" type="text" id="pressureFromNumber">
                    </div>
                    <div class="col-md-6">
                        <span id="pressureToNumber">1</span>
                    </div>
                </div>
                <div class="row">
                    <div class="col-md-6">
                        <select class="form-control" id="pressureFromUnit" size="15">
                            ${pressure}
                        </select>
                    </div>
                    <div class="col-md-6">
                        <select class="form-control" id="pressureToUnit" size="15">
                            ${pressure}
                        </select>
                    </div>
                </div>
            </form>
        </div>
        <div id="force" class="tab-pane">
            <h4>Force Converter</h4>
            <form role="form">
                <div class="row">
                    <div class="col-md-6">
                        From
                    </div>
                    <div class="col-md-6">
                        To
                    </div>
                </div>
                <div class="row">
                    <div class="col-md-6">
                        <input value="1" type="text" id="forceFromNumber">
                    </div>
                    <div class="col-md-6">
                        <span id="forceToNumber">1</span>
                    </div>
                </div>
                <div class="row">
                    <div class="col-md-6">
                        <select class="form-control" id="forceFromUnit" size="15">
                            ${force}
                        </select>
                    </div>
                    <div class="col-md-6">
                        <select class="form-control" id="forceToUnit" size="15">
                            ${force}
                        </select>
                    </div>
                </div>
            </form>
        </div>
        <div id="distance" class="tab-pane">
            <h4>Distance Converter</h4>
            <form role="form">
                <div class="row">
                    <div class="col-md-6">
                        From
                    </div>
                    <div class="col-md-6">
                        To
                    </div>
                </div>
                <div class="row">
                    <div class="col-md-6">
                        <input value="1" type="text" id="distanceFromNumber">
                    </div>
                    <div class="col-md-6">
                        <span id="distanceToNumber">1</span>
                    </div>
                </div>
                <div class="row">
                    <div class="col-md-6">
                        <select class="form-control" id="distanceFromUnit" size="15">
                            ${distance}
                        </select>
                    </div>
                    <div class="col-md-6">
                        <select class="form-control" id="distanceToUnit" size="15">
                            ${distance}
                        </select>
                    </div>
                </div>
            </form>
        </div>
    </div>
    <script>
        $('#converter a').click(function (e) {
            e.preventDefault()
            $(this).tab('show')
        })
    </script>
</%block>