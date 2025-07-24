#!/usr/bin/env python3
import http.server
import socketserver
import webbrowser
import os

PORT = 3001

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=os.getcwd(), **kwargs)

try:
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        print(f"Server running at http://localhost:{PORT}")
        print(f"View the demo at: http://localhost:{PORT}/frontend/demo.html")
        httpd.serve_forever()
except KeyboardInterrupt:
    print("\nServer stopped.")