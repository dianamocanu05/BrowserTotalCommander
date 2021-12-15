import os
from http.server import HTTPServer, CGIHTTPRequestHandler

os.chdir('.')
server_object = HTTPServer(server_address=('127.0.0.1', 80), RequestHandlerClass=CGIHTTPRequestHandler)
print('Server running on 127.0.0.1...')
server_object.serve_forever()
