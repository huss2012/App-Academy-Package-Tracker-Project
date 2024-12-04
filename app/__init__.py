from flask import Flask, render_template
from .config import Config
from .routes import index, new_package
from flask_migrate import Migrate
from .models import db

app = Flask(__name__)
app.config.from_object(Config)
app.register_blueprint(index.bp)
app.register_blueprint(new_package.bp)
db.init_app(app)
Migrate(app, db)
