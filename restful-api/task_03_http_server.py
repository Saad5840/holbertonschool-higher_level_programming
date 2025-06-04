#!/usr/bin/env python3
import http.server
import socketserver
import json


class SimpleHTTPRequestHandler(http.server.BaseHTTPRequestHandler):
    def _set_headers(self, status_code=200, content_type="text/plain"):
        self.send_response(status_code)
        self.send_header("Content-type", content_type)
        self.end_headers()

    def do_GET(self):
        if self.path == "/":
            self._set_headers()
            self.wfile.write(b"Hello, this is a simple API!")
        elif self.path == "/data":
            data = {"name": "John", "age": 30, "city": "New York"}
            self._set_headers(200, "application/json")
            self.wfile.write(json.dumps(data).encode("utf-8"))
        elif self.path == "/status":
            self._set_headers()
            self.wfile.write(b"OK")
        elif self.path == "/info":
            info = {"version": "1.0", "description": "A simple API built with http.server"}
            self._set_headers(200, "application/json")
            self.wfile.write(json.dumps(info).encode("utf-8"))
        else:
            self._set_headers(404, "application/json")
            error = {"error": "Endpoint not found"}
            self.wfile.write(json.dumps(error).encode("utf-8"))


if __name__ == "__main__":
    PORT = 8000
    Handler = SimpleHTTPRequestHandler
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        print(f"Serving at http://localhost:{PORT}")
        httpd.serve_forever()
