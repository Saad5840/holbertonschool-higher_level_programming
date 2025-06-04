import http.server
import json

class SimpleHTTPRequestHandler(http.server.BaseHTTPRequestHandler):

    def _set_headers(self, status_code=200, content_type="text/plain"):
        self.send_response(status_code)
        self.send_header("Content-Type", content_type)
        self.end_headers()

    def do_GET(self):
        if self.path == "/":
            self._set_headers(200, "text/plain")
            self.wfile.write(b"Hello, this is a simple API!")
        
        elif self.path == "/data":
            self._set_headers(200, "application/json")
            data = {"name": "John", "age": 30, "city": "New York"}
            self.wfile.write(json.dumps(data).encode("utf-8"))
        
        elif self.path == "/info":
            self._set_headers(200, "application/json")
            info = {"version": "1.0", "description": "A simple API built with http.server"}
            self.wfile.write(json.dumps(info).encode("utf-8"))
        
        elif self.path == "/status":
            self._set_headers(200, "text/plain")
            self.wfile.write(b"OK")
        
        else:
            self._set_headers(404, "text/plain")
            self.wfile.write(b"Endpoint not found")

def run(server_class=http.server.HTTPServer, handler_class=SimpleHTTPRequestHandler):
    server_address = ('', 8000)  # Listen on all interfaces, port 8000
    httpd = server_class(server_address, handler_class)
    print("Starting http.server on port 8000...")
    httpd.serve_forever()

if __name__ == '__main__':
    run()
