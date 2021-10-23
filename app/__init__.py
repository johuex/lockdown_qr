from flask import Flask
from .config import Config



app = Flask(__name__)
app.config.from_object(Config)
app.jinja_env.trim_blocks = True
app.jinja_env.lstrip_blocks = True


from app import routes
