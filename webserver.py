# Import the http.server module
import http.server

# Specify the port you want to use (e.g., 8000)
port = 8000

# Change to the directory you want to serve files from (default is the current directory)
web_dir = '.'  # Change this to the desired directory

# Create an HTTP server
with http.server.HTTPServer(('', port), http.server.SimpleHTTPRequestHandler) as server:
    print(f'Starting server on port {port}...')
    # Start the server
    server.serve_forever()
