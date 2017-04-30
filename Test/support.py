import os
from google.appengine.ext.webapp import template

# render a page using the given template and return as a string
def render_page(tname = 'index.html', values = { }):
    templ = os.path.join(
          os.path.dirname(__file__),
          'templates/' + tname)
    if not os.path.isfile(templ):
        return 'Error:  Template ' + tname + 'not found.'

    return template.render(templ, values)
