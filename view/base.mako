<!doctype html>
<html>
    <head>
        <title>
        <%block name="title">
            Civil Engineering Toolkit
        </%block>
        </title>
        <!-- CSS -->
        <link href="/static/bootstrap/css/bootstrap.min.css"
              rel="stylesheet" type="text/css" />
        <link href="/static/bootstrap/css/bootstrap.min.css"
              rel="stylesheet" type="text/css" />
        <%block name="css">
        <link href="/static/tes.txt"
              rel="stylesheet" type="text/css" />
        </%block>

        <!-- JS -->
        <script src="/static/jquery-ui/external/jquery/jquery.min.js"></script>
        <script src="/static/bootstrap/js/bootstrap.min.js"></script>
        <%block name="javascript">

        </%block>
    </head>
    <body>
        <%include file="navigation.mako"/>
        <div>
            <%block name="content">
                No content
            </%block>
        </div>
    </body>
</html>