import webapp2

class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/html'
	f = open('index.html', 'r')
	for line in f:
        	self.response.write(line)

app = webapp2.WSGIApplication([
    ('/', MainPage),
], debug=True)
