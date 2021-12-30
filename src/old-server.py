from http.server import HTTPServer, BaseHTTPRequestHandler
from src.routes import routes
from src.utils import create_html_list
from src.file_manager import get_file_tree

# HOST_NAME = '127.0.0.1'
HOST_NAME = 'localhost'
PORT = 80


class Handler(BaseHTTPRequestHandler):
    def do_HEAD(self):
        return

    def do_GET(self):
        self.respond()

    def do_POST(self):
        return

    def handle_http(self, status, content_type):
        status = 200
        if self.path in routes:
            route_content = routes[self.path]['path']
            content_type = routes[self.path]['type']
            if self.path.endswith('.png') or self.path.endswith('.ico'):
                response_content = open(route_content, 'rb')
                response_content = response_content.read()
                self.send_response(status)
                self.send_header('Content - type', content_type)
                self.end_headers()
                return response_content
            else:
                response_content = open(route_content, encoding="utf-8")
                response_content = response_content.read()
        else:
            content_type = "text/plain"
            response_content = "404 Not Found"

        self.send_response(status)
        self.send_header('Content - type', content_type)
        self.end_headers()
        return bytes(response_content, "UTF - 8")

    def respond(self):
        content = self.handle_http(200, 'text / templates')
        self.wfile.write(content)


server_object = HTTPServer(server_address=(HOST_NAME, PORT), RequestHandlerClass=Handler)
print('Server running on 127.0.0.1...')
server_object.serve_forever()
