from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import cgi

from database_setup import DecBase, Sites, Categories, Items, Sales, Keycode
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///ecommanalyser.db')
DecBase.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()


class webServerHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        try:
		if self.path.endswith("/sites/new"):
			self.send_response(200)
			self.send_header('Content-type', 'text/html')
			self.end_headers()
			output = ""
			output += "<html><body>"
			output += "<h1>Make a New Site</h1>"
			output += "<form method='do_POST' enctype='multipart/form-data' action='/sites/new'>"
			output += "<input name = 'newSiteName' type = 'text' placeholder = 'New Site Name' > "
			output += "<input type='submit' value='Create'>"
			output += "</form></body></html>"
			self.wfile.write(output)
			return

		if self.path.endswith("/sites"):
			sites = session.query(Sites).all()
			output = ""
			output += "<html><body>"
			output += "<a href ='/sites/new'> New entry </a></br>"
			self.send_response(200)
			self.send_header('Content-type', 'text/html')
			self.end_headers()

			for site in sites:
				output += site.site_name
				output += "</br></br></br>"
				output += "<a href ='#' >Edit </a> "
				output += "</br>"
				output += "<a href =' #'> Delete </a>"
				output += "</br></br></br>"
			output += "</body></html>"
			self.wfile.write(output)
               		return
        except IOError:
            self.send_error(404, 'File Not Found: %s' % self.path)

	def do_POST(self):
		try:
			if self.path.endswith("/sites/new"):
				ctype, pdict = cgi.parse_header(self.headers.getheader('content-type'))
				if ctype == 'multipart/form-data':
					fields = cgi.parse_multipart(self.rfile, pdict)
					messagecontent = fields.get('newSiteName')
					newSite = Sites(s_id='wsss06',site_name=messagecontent[0])
					session.add(newSite)
					session.commit()
					self.send_response(301)
					self.send_header('Content-type', 'text/html')
					self.send_header('Location', '/sites')
					self.end_headers()
		except:
			pass
			
def main():
    try:
        server = HTTPServer(('localhost', 8080), webServerHandler)
        print 'Web server running...open localhost:8080/sites in your browser'
        server.serve_forever()
    except KeyboardInterrupt:
        print '^C received, shutting down server'
        server.socket.close()

if __name__ == '__main__':
	main()
