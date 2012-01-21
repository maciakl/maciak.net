import os
from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.ext.webapp import template


class MainPage(webapp.RequestHandler):

	def get(self, p):

		page = self.get_page_name(p)

		template_values = { "page" : page, p: "first", };


		if p=="guid":
			from myutil import gen_guid
			template_values["guid"] = gen_guid()

		if p=="ascii":
			from myutil import ascii_table
			table = ascii_table()
			template_values["lower"] = table["lowercase"]
			template_values["upper"] = table["uppercase"]
			template_values["digits"] = table["digits"]
			template_values["punctuation"] = table["punctuation"]

		self.render_page(template_values)

	def post(self, p):

		page = self.get_page_name(p)

		template_values = { "page" : page, p: "first", }

		if p=="rot13":
			template_values["rot"] = self.request.get('rot13').encode('rot13')

		if p=="hash":
			from myutil import get_hashvalues
			template_values["hash"] = get_hashvalues(self.request.get('hashstring'))

		if p=="b64":
			import base64
			template_values["b64encode"] = base64.b64encode(self.request.get('base64encode'))
			template_values["b64decode"] = base64.b64decode(self.request.get('base64decode'))

		if p=="lipsum":
			from lorem_ipsum import paragraphs
			para = int(self.request.get('para')) if self.request.get('para') else 5
			if para > 100: para = 100
			template_values["lorem"] = paragraphs(para)

		if p=="pass":
			from password_gen import gen_passwords
			howmany = int(self.request.get('howmany')) if self.request.get('howmany') else 10
			howlong = int(self.request.get('howlong')) if self.request.get('howlong') else 8
			template_values["pwds"] = gen_passwords(howmany, howlong)

		self.render_page(template_values)

	def get_page_name(self, p):
	
		if p:
			page = p + ".html"
		else:
			p = "main"
			page = p + ".html"

		if not os.path.exists(page):
			page = "404.html"

		return page

	def render_page(self, template_values):

		path = os.path.join(os.path.dirname(__file__), 'index.html')
		self.response.out.write(template.render(path, template_values))


application = webapp.WSGIApplication([(r'/(.*)', MainPage)],debug=True)

def main():
	run_wsgi_app(application)

if __name__ == "__main__":
	main()
