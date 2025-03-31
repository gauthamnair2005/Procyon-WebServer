from http.server import SimpleHTTPRequestHandler, HTTPServer
import os
import mimetypes
import subprocess

class MyHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            if os.path.isfile('index.lsp'):
                self.path = '/index.lsp'
            elif os.path.isfile('index.html'):
                self.path = '/index.html'
            elif os.path.isfile('index.php'):
                self.path = '/index.php'
            else:
                print("Error: index.lsp, index.html, or index.php not found.")
                self.send_error(404, 'File Not Found: index.lsp, index.html, or index.php')
                return
        
        try:
            file_path = os.getcwd() + self.path
            if os.path.isdir(file_path):  # Check if the path is a directory
                self.list_directory(file_path)  # List the directory contents
            elif os.path.isfile(file_path):
                if file_path.endswith('.lsp'):
                    output = self.execute_lsp(file_path)
                    self.send_response(200)
                    self.send_header('Content-type', 'text/html')
                    self.end_headers()
                    self.wfile.write(output.encode())
                elif file_path.endswith('.php'):
                    output = self.execute_PHP(file_path)
                    self.send_response(200)
                    self.send_header('Content-type', 'text/html')
                    self.end_headers()
                    self.wfile.write(output.encode())
                else:
                    mime_type, _ = mimetypes.guess_type(file_path)
                    self.send_response(200)
                    self.send_header('Content-type', mime_type)
                    self.end_headers()
                    with open(file_path, 'rb') as file:
                        self.wfile.write(file.read())
            else:
                print(f"Error: File Not Found: {self.path}")
                self.send_error(404, 'File Not Found: %s' % self.path)
        except Exception as e:
            print(f"Error: {str(e)}")
            self.send_error(500, 'Internal Server Error: %s' % str(e))

    def list_directory(self, path):
        """Helper method to list directory contents."""
        try:
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            items = os.listdir(path)
            output = "<html><body><h1>Directory listing for %s</h1><ul>" % self.path
            for item in items:
                item_path = os.path.join(self.path, item)
                if os.path.isdir(os.path.join(path, item)):
                    output += f'<li><a href="{item_path}/">{item}/</a></li>'
                else:
                    output += f'<li><a href="{item_path}">{item}</a></li>'
            output += "</ul></body></html>"
            self.wfile.write(output.encode())
        except Exception as e:
            print(f"Error: {str(e)}")
            self.send_error(500, 'Error listing directory: %s' % str(e))

    def execute_lsp(self, file_path):
        result = subprocess.run(['python', 'lsp.py', file_path], capture_output=True, text=True)
        if result.returncode == 0:
            return result.stdout
        else:
            print(f"Error executing lsp script")
            return f"<html><body><h1>Error executing lsp script</h1><pre>{result.stderr}</pre></body></html>"

    def execute_PHP(self, file_path):
        result = subprocess.run(['php', file_path], capture_output=True, text=True)
        if result.returncode == 0:
            return result.stdout
        else:
            print(f"Error executing PHP script")
            return f"<html><body><h1>Error executing PHP script</h1><pre>{result.stderr}</pre></body></html>"

def run(server_class=HTTPServer, handler_class=MyHandler):
    software_name = "Procyon WebServer"
    version = "1.0.2"
    developer = "Gautham Nair"
    print(f"{software_name} {version}")
    print(f"Developed by: {developer}")
    print("-" * 80)

    try:
        port = int(input().strip())
        server_address = ('', port)
        httpd = server_class(server_address, handler_class)
        print(f"Server started at: http://localhost:{port}")
        print("-" * 80)
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("Server stopped by user.")
    except Exception as e:
        print(f"Error: {str(e)}")
    finally:
        print("Server shutting down...")

if __name__ == "__main__":
    run()