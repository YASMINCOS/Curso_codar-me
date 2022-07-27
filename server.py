from cgitb import html
from email import header
from http import server
from http.server import BaseHTTPRequestHandler, HTTPServer

class SimpleHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send-header("Content-Type","text/html; charset=utf-8")
        self.send_header("Teste","abc")
        self.end_headers()
        data= f"""""
        <html>
         <head>
            <title>Olá, Mundo.</title>
        </head>
        <body>
         <p> Testando o servidor HTTP</p>
         <p>Diretório: {self.path}</p>
        </body>
        </html>
        """.encode()
        self.wfile.write(data)

server=HTTPServer(('localhost',8000),SimpleHandler)
server.serve_forever()