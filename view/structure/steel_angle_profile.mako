<%inherit file="../base.mako"/>

<%block name="content">
    <%include file="steel_nav_profile.mako"/>
    ${section(properties)}
</%block>
<%def name="section(properties)">
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
                ${th("Dimension")}
                ${th("t")}
                ${th("r<sub>1</sub>")}
                ${th("r<sub>2</sub>")}
                ${th("Area")}
                ${th("")}
                ${th("Ixx")}
                ${th("Iyy")}
                ${th("Sx")}
                ${th("Sy")}
                ${th("ix")}
                ${th("iy")}
            </tr>
            <tr>
                ${th("mm")}
                ${th("mm")}
                ${th("mm")}
                ${th("mm")}
                ${th("cm<sup>2</sup>")}
                ${th("kg/m")}
                ${th("cm<sup>4</sup>")}
                ${th("cm<sup>4</sup>")}
                ${th("cm<sup>3</sup>")}
                ${th("cm<sup>3</sup>")}
                ${th("cm")}
                ${th("cm")}
            </tr>
        </thead>
        <tbody>
            % for property in properties:
            <tr>
                <td class="text-left">${property[0]}</td>
                <td>${property[1]}</td>
                <td>${property[2]}</td>
                <td>${property[3]}</td>
                <td>${property[4]}</td>
                <td>${property[5]}</td>
                <td>${property[6]}</td>
                <td>${property[7]}</td>
                <td>${property[8]}</td>
                <td>${property[9]}</td>
                <td>${property[10]}</td>
                <td>${property[11]}</td>
            </tr>
            % endfor
        </tbody>
    </table>
</%def>

<%def name="th(val, colspan='1')">
    <th class="text-center" colspan="${colspan}">${val}</th>
</%def>