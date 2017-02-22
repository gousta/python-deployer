import http.server
import socketserver
import io

class Handler(http.server.SimpleHTTPRequestHandler):

    def do_POST(self):
        path = self.path.replace('/deploy', '')
        path = path + '/deploy.txt'
        print(path)
        
        commands_file = open(path, 'r')
        for command in commands_file.readlines():
            print(command)
        commands_file.close()

        # Construct a server response.
        self.send_response(200)
        self.end_headers()
        return


print('Server listening on port 8080...')
httpd = socketserver.TCPServer(('', 8080), Handler)
httpd.serve_forever()