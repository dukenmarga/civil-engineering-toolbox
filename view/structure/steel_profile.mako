<%inherit file="../base.mako"/>

<%block name="content">
    <h4>IWF Steel Profile</h4>
    <span class="label label-info">Click header to sort</span>
    <table class="table text-center table-bordered table-striped table-hover">
        <thead>
            <tr>
                <th class="text-center" colspan="4">Profile</th>
                <th class="text-center">Section</th>
                <th class="text-center">Unit Mass</th>
                <th class="text-center" colspan="2">
                    2<sup>nd</sup> Moment of Inertia</th>
                <th class="text-center" colspan="2">
                    Modulus of Section</th>
                <th class="text-center" colspan="2">
                    Radius of Gyration</th>
            </tr>
            <tr>
                <th class="text-center">Dimension</th>
                <th class="text-center">tw</th>
                <th class="text-center">tf</th>
                <th class="text-center">r</th>
                <th class="text-center">Area</th>
                <th class="text-center"></th>
                <th class="text-center">Ixx</th>
                <th class="text-center">Iyy</th>
                <th class="text-center">Sx</th>
                <th class="text-center">Sy</th>
                <th class="text-center">ix</th>
                <th class="text-center">iy</th>
            </tr>
            <tr>
                <th class="text-center">mm</th>
                <th class="text-center">mm</th>
                <th class="text-center">mm</th>
                <th class="text-center">mm</th>
                <th class="text-center">cm<sup>2</sup></th>
                <th class="text-center">kg/m</th>
                <th class="text-center">cm<sup>4</sup></th>
                <th class="text-center">cm<sup>4</sup></th>
                <th class="text-center">cm<sup>3</sup></th>
                <th class="text-center">cm<sup>3</sup></th>
                <th class="text-center">cm</th>
                <th class="text-center">cm</th>
            </tr>
        </thead>
        <tbody>
            % for properties in geometricProperties:
            <tr>
                <td class="text-left">${properties[0]}</td>
                <td>${properties[1]}</td>
                <td>${properties[2]}</td>
                <td>${properties[3]}</td>
                <td>${properties[4]}</td>
                <td>${properties[5]}</td>
                <td>${properties[6]}</td>
                <td>${properties[7]}</td>
                <td>${properties[8]}</td>
                <td>${properties[9]}</td>
                <td>${properties[10]}</td>
                <td>${properties[11]}</td>
            </tr>
            % endfor
        </tbody>
    </table>
</%block>