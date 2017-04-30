from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from minidb import MiniDB
from datetime import datetime

class uvapi(webapp.RequestHandler):

    def get(self):
        try:
            uv = int(self.request.get('uv'))
            ir = int(self.request.get('ir'))
            
            miniDB = MiniDB()
            miniDB.uv = str(uv)
            miniDB.ir = str(ir)
            miniDB.time = str(datetime.now())
            miniDB.put()

            self.response.out.write("<html><body><p>%d + %d = %d</p></body></html>" %
                                    (uv, ir, uv + ir))
        except (TypeError, ValueError):
            self.response.out.write("<html><body><p>Invalid inputs</p></body></html>")

application = webapp.WSGIApplication([('/uvapi', uvapi)], debug=True)


def main():
    run_wsgi_app(application)

if __name__ == "__main__":
    main()
