#!/usr/bin/env python3
"""Serve the Flag Practice site at http://localhost:8793 (needed so the flag images can be analysed)."""
import http.server, socketserver, os, webbrowser
os.chdir(os.path.dirname(os.path.abspath(__file__)))
PORT = 8793
socketserver.TCPServer.allow_reuse_address = True
with socketserver.TCPServer(("", PORT), http.server.SimpleHTTPRequestHandler) as s:
    print(f"Flag Practice running at http://localhost:{PORT}  (Ctrl+C to stop)")
    webbrowser.open(f"http://localhost:{PORT}")
    s.serve_forever()
