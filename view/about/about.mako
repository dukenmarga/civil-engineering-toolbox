<%inherit file="../base.mako"/>

<%block name="content">
    <h4>civil-engineering-toolbox</h4>
    <p><strong>civil-engineering-toolbox</strong> is collection of small programs to help civil
    engineer to solve small to medium size and common problems found in
    engineering world in order to solve the big problems. This software can
    be used as a problem-solver, or to give quick estimation.</p>
    <p>Website: <a href="https://github.com/dukenmarga/civil-engineering-toolbox">
            https://github.com/dukenmarga/civil-engineering-toolbox
    </a>
    </p>
    <div class="col-md-4">
        <strong>Programmer:</strong>
        <ol>
            <li data-toggle="popover" class="info" title="Duken Marga Turnip"
                data-content="Civil Engineer<br>"
                data-placement="auto">
                <a href="http://duken.info">Duken Marga Turnip</a>
            </li>
        </ol>
    </div>
    <div class="col-md-4">
        <strong>Contributor for Calculation:</strong>
        <ol>
            <li data-toggle="popover" class="info" title="Duken Marga Turnip"
                data-content="Civil Engineer<br>"
                data-placement="auto">
                <a href="http://duken.info">Duken Marga Turnip</a>
            </li>
        </ol>
    </div>
    <div class="col-md-4">
        <strong>Contributor for Translator:</strong>
        <ol>

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