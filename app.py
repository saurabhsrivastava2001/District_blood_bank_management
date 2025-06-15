from flask import Flask
from routes.donors import donors_bp
from routes.hospitals import hospitals_bp
#from routes.auth import auth_bp

app = Flask(__name__)
app.secret_key = "hellosaurabh"  # Used for sessions (e.g., login system)

# Registering blueprints
app.register_blueprint(donors_bp)
app.register_blueprint(hospitals_bp)
#app.register_blueprint(auth_bp)

@app.route('/')
def home():
    return "Welcome to the District Blood Bank Management System!"

if __name__ == '__main__':
    app.run(debug=True)
