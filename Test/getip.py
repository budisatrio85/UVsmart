from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from minidb import MiniDB
import json 

class getip(webapp.RequestHandler):

    def get(self):
        try:
            text="["
            allDb = MiniDB.all()
            allDb.order('time')
            i = 0
            for tes in allDb.run(limit=10):
                uv = float(tes.uv)/100
                text+="[%s, %s]," % (i, uv)
                i = i+1
            text = text[:-1]
            text+="]"
            self.response.out.write(text)
        except (TypeError, ValueError):
            self.response.out.write("<html><body><p>Invalid inputs</p></body></html>")

application = webapp.WSGIApplication([('/getip', getip)], debug=True)


def main():
    run_wsgi_app(application)

if __name__ == "__main__":
    main()
