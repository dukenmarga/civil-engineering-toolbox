<%inherit file="../base.mako"/>

<%block name="content">
    <div class="col-md-8">
        <h4>List of Applications</h4>
        <ul>
            <li>Structure
                <ul>
                    <li><a href="/structure/steel/profile">Steel Section Tables</a></li>
                    <li><a href="/structure/concrete/slab-two-ways">Concrete Two ways slab</a></li>
                    <li><a href="/structure/concrete/flexural-analysis">Concrete Flexural Analysis</a></li>
                    <li><a href="/structure/earthquake/response-spectrum">Response Spectrum</a></li>
                </ul>
            </li>
            <li>Geotechnic
                <ul>
                    <li><a href="/geotechnic/surcharge/point-load">Surcharge Point Load</a></li>
                </ul>
                <ul>
                    <li><a href="/geotechnic/surcharge/strip-load">Surcharge Strip Load</a></li>
                </ul>
            </li>
            <li>Math
                <ul>
                    <li><a href="/math/unit-converter">Unit Converter</a></li>
                </ul>
            </li>
        </ul>
    </div>
</%block>