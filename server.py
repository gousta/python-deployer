import http.server
import socketserver
import io
import os

class Handler(http.server.SimpleHTTPRequestHandler):

    def do_POST(self):
        path = self.path.replace('/deploy', '')

        commands_file = open(path + '/deploy_commands.txt', 'r')
        commands = commands_file.read().splitlines()
        commands_file.close()

        commands = ' && '.join(commands)
        commands = 'cd ' + path + ' && ' + commands.strip()

        os.system(commands + ' > ' + path + '/deploy_latest.txt')

        # Construct a server response.
        self.send_response(200)
        self.end_headers()
        return


print('Server listening on port 8080...')
httpd = socketserver.TCPServer(('', 8080), Handler)
httpd.serve_forever()