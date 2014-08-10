<%inherit file="../base.mako"/>

<%block name="content">
    <table>
        <thead>
            <tr>
                <td>Profile</td>
                <td>Iy</td>
                <td>Testing3</td>
                <td>Testing4</td>
            </tr>
        </thead>
        <tbody>
            % for profileName, properties in geometricProperties.items():
            <tr>
                %for k, v in properties.items():
                    <td>${v}</td>
                %endfor
            </tr>
            % endfor
        </tbody>
    </table>
</%block>