from src import view

def error_404(status, message,traceback, version):
    template = view.lookup.get_template('about/404.mako')
    return template.render()
