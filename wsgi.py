import os
from wsgiref.simple_server import make_server
        
from app import api

if __name__ == "__main__":

try:
        port = sys.argv[1]
except:
        port = 8015
        
    with make_server("", port, api) as httpd:
        # Serve until process is killed
        logger.debug("Start wsgi web-server")
        logger.debug(f"Listening Port {port}...")
        
        httpd.serve_forever()
