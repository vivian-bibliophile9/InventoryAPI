import subprocess
import sys

subprocess.call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
