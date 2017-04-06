# Python Deployer
Webhook script that runs your commands for automatic deployment when you push a commit.

Note: Requires Python 3 to work

### Starting Script in Background
`nohup python3 /path/to/project/server.py &`

### Endpoint
`http://YOUR_SERVER_IP:8080/deploy{FULL_PATH_TO_PROJECT}`
