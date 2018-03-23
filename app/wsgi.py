import sys
sys.path.insert(0, "opt/dj/project/wsgi")
from app import app as application

if __name__ == "__main__":
    application.run()

