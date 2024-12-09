from http.server import SimpleHTTPRequestHandler, HTTPServer
import os
import mimetypes

class MyHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.path = '/index.html'
        
        try:
            file_path = os.getcwd() + self.path
            if os.path.isfile(file_path):
                mime_type, _ = mimetypes.guess_type(file_path)
                self.send_response(200)
                self.send_header('Content-type', mime_type)
                self.end_headers()
                with open(file_path, 'rb') as file:
                    self.wfile.write(file.read())
            else:
                self.send_error(404, 'File Not Found: %s' % self.path)
        except Exception as e:
            self.send_error(500, 'Internal Server Error: %s' % str(e))

def run(server_class=HTTPServer, handler_class=MyHandler, port=8080):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f'Starting httpdserver on port {port}...')
    httpd.serve_forever()

if __name__ == "__main__":
    run(port=8088)