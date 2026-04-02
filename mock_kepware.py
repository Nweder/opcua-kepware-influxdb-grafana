from http.server import BaseHTTPRequestHandler, HTTPServer
import json
from urllib.parse import urlparse, parse_qs
import random


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        parsed = urlparse(self.path)
        if parsed.path == '/read':
            qs = parse_qs(parsed.query)
            ids = qs.get('ids', [])
            response = []
            for id in ids:
                if 'temp' in id.lower() or 'temperature' in id.lower():
                    val = round(20 + random.random() * 10, 2)
                else:
                    val = random.randint(0, 1)
                response.append({"id": id, "v": val, "s": "good"})
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps(response).encode('utf-8'))
        else:
            self.send_response(404)
            self.end_headers()


if __name__ == '__main__':
    server = HTTPServer(('0.0.0.0', 5000), Handler)
    print('Mock Kepware running on http://0.0.0.0:5000')
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print('\nShutting down mock server')
        server.server_close()
