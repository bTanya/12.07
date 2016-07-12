from socketserver import TCPServer, StreamRequestHandler
import  socket

class Handler(StreamRequestHandler):
    def handle(self):
        d = self.rfile.readline()
        self.wfile.write(d)

serv = TCPServer((socket.gethostname(), 1212),Handler)
serv.serve_forever()
serv.shutdown()