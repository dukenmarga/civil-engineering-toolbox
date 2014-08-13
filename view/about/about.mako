<%inherit file="../base.mako"/>

<%block name="content">
    <h4>civil-engineering-toolbox</h4>
    <div class="col-md-4">
        <strong>Programmer:</strong>
        <ol>
            <li data-toggle="popover" class="info" title="Duken Marga Turnip"
                data-content="Indonesia<br>
                Structural Engineer<br>
                http://duken.info" data-placement="auto">Duken Marga Turnip</li>
            <!--li data-toggle="popover" class="info" title="Duken Marga Turnip"
                data-content="Indonesia<br>
                Institut Teknologi Bandung<br>
                http://duken.info" data-placement="auto">Duken Marga Turnip</li-->
        </ol>
    </div>
    <div class="col-md-4">
        <strong>Contributor for Calculation:</strong>
        <ol>
            <li data-toggle="popover" class="info" title="Duken Marga Turnip"
                data-content="Indonesia<br>
                Structural Engineer<br>
                http://duken.info" data-placement="auto">Duken Marga Turnip</li>
        </ol>
    </div>
    <div class="col-md-4">
        <strong>Contributor for Translator:</strong>
        <ol>
            <li>Your Name</li>
        </ol>
            <script>
                $('.info').popover({
                    trigger: 'hover',
                    html: true,
                    delay: { show: 100, hide: 100 }
                })
            </script>
    </div>
</%block>