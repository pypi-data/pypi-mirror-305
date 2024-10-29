import http.server
import socketserver
import os

def host_website(directory: str = ".", port: int = 8000, host: str = "localhost"):
    """
    Starts a web server to host static files from the specified directory.
    
    Args:
        directory (str): The path to the directory containing the website files. Defaults to the current directory.
        port (int): The port number to run the server on. Default is 8000.
        host (str): The hostname or IP address to bind the server to. Default is "localhost".
    
    Example:
        host_website("C:/path/to/your/website", port=8080, host="0.0.0.0")
    """
    os.chdir(directory)
    
    handler = http.server.SimpleHTTPRequestHandler
    
    with socketserver.TCPServer((host, port), handler) as httpd:
        print(f"Hosting website at http://{host}:{port}")
        print("Press Ctrl+C to stop the server.")
        httpd.serve_forever()

