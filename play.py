import webapp2
form="""
<html>
<form action="/testform">
        <input name="q">
        <input type="submit">
</form>
</html>
"""
class MainPage(webapp2.RequestHandler):
        def get(self):
                #self.response.headers['Content-Type'] = 'text/plain'
                self.response.out.write(form)
        
class TestHandler(webapp2.RequestHandler):
        def get(self):
                q = self.request.get("q")
                self.response.out.write(q)
    
app = webapp2.WSGIApplication([('/', MainPage)], debug=True)
