import os
import subprocess
import streamlit

PORT = os.environ.get("PORT", 8501)
cmd = f"streamlit run app.py --server.port {PORT} --server.address 0.0.0.0 --server.headless True"

subprocess.run(cmd, shell=True, check=True)