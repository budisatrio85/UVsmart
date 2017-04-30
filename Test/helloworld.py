from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from support import render_page

class MainPage(webapp.RequestHandler):
    
    
    def get(self):
        web_page = render_page('index.html')
            
        self.response.out.write(web_page)


application = webapp.WSGIApplication([('/', MainPage)], debug=True)


def main():
    run_wsgi_app(application)

if __name__ == "__main__":
    main()
