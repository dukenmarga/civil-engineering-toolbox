<%inherit file="../base.mako"/>

<%block name="content">
    <div class="col-md-8">
        <h4>List of Applications</h4>
        <ul>
            <li>Structure
                <ul>
                    <li><a href="/structure/steel/profile">Steel Section Tables</a></li>
                    <li><a href="/structure/concrete/slab-two-ways">Concrete Two Ways Slab</a></li>
                    <li><a href="/structure/concrete/flexural-analysis">Concrete Flexural Analysis</a></li>
                    <li><a href="/structure/concrete/oneway-shear-design">Concrete One-Way Shear Design</a></li>
                    <li><a href="/structure/concrete/twoway-shear-design">Concrete Two-Way Shear Design</a></li>
                    <li><a href="/structure/earthquake/response-spectrum">Response Spectrum</a></li>
                </ul>
            </li>
            <li>Geotechnic
                <ul>
                    <li><a href="/geotechnic/surcharge/point-load">Surcharge Point Load</a></li>
                    <li><a href="/geotechnic/surcharge/strip-load">Surcharge Strip Load</a></li>
                    <li><a href="/geotechnic/shallow-foundation/analysis">Shallow Foundation Analysis</a></li>
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