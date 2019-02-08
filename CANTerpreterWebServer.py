#Author: Justin Schneider
#Created: 10:26PM February 7, 2019
#Purpose: Display current CAN status information

from http.server import HTTPServer, BaseHTTPRequestHandler
import time
import os

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        logfile = open("CanReadings.txt", "rb")
        while True:
            file_data = logfile.read(32768)
            if file_data is None or len(file_data) == 0:
                break
            self.wfile.write(file_data)
        logfile.close()

if __name__ == '__main__':
	# NOTE:IP BELOW MUST MATCH RPI Internal IP ADDRESS! NOT 'localhost'!
	httpd = HTTPServer(('192.168.50.143', 7777), SimpleHTTPRequestHandler)
	httpd.serve_forever()
