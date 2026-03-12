from waitress import serve
import api
import os

host = os.environ.get("HOST", "0.0.0.0")
port = int(os.environ.get("PORT", 8080))
debug = os.environ.get("DEBUG", "false").lower() == "true"

print(f"Backend: {host}:{port}, debug: {debug}")

serve(api.app, host=host, port=port)