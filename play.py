import webapp2
form="""
<html>
<form action="http://www.google.com/search">
        <input name="q">
        <input type="submit">
</form>
</html>
"""
class MainPage(webapp2.RequestHandler):
  def get(self):
    #self.response.headers['Content-Type'] = 'text/plain'
    self.response.out.write(form)
    
app = webapp2.WSGIApplication([('/', MainPage)], debug=True)
