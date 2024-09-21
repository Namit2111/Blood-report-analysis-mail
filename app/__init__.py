from flask import Flask
from app.report import report
from flask_jwt_extended import JWTManager, create_access_token, jwt_required

app = Flask(__name__)


app.config['JWT_SECRET_KEY'] = 'your_secret_key'  # Change this to a random secret key
jwt = JWTManager(app)


app.register_blueprint(report)
