<!doctype html>
<html>
    <head>
        <title>
        <%block name="title">
            Civil Engineering Toolbox
        </%block>
        </title>

        <!-- Meta -->
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
        <meta http-equiv="X-UA-Compatible" content="IE=edge">

        <!-- CSS -->
        ${css_file("bootstrap/css/bootstrap.min.css")}
        ${css_file("font-awesome/css/font-awesome.min.css")}
        ${css_file("jquery-ui/jquery-ui.min.css")}
        ${css_file("jquery-ui/jquery-ui.theme.min.css")}
        ${css_file("css/cousine.css")}
        ${css_file("css/custom.css")}
        <%block name="css">
        </%block>

        <!-- JS -->
        ${js_file("jquery-ui/external/jquery/jquery.min.js")}
        ${js_file("bootstrap/js/bootstrap.min.js")}
        ${js_file("js/jquery-table-sorter.min.js")}
        ${js_file("js/jquery-floatThead.min.js")}
        ${js_file("jquery-ui/jquery-ui.min.js")}
        ${js_file("js/global.js")}
        <%block name="javascript">
        </%block>
    </head>
    <body>
        <div class="container-fluid">
            <%include file="navigation.mako"/>
            <div class="row content">
                <div class="row col-md-10 col-md-offset-1">
                    <%block name="content">
                        No content
                    </%block>
                </div>
            </div>
            <div class="row footer">
                <div class="col-md-4 col-md-offset-6">
                    <br>
                </div>
            </div>
        </div>
    </body>
</html>

<%def name="css_file(url)">
    <link href="/static/${url}"
          rel="stylesheet" type="text/css" />
</%def>

<%def name="js_file(url)">
    <script type="text/javascript" src="/static/${url}"></script>
</%def>
