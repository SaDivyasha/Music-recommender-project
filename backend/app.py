from flask import Flask
from flask_cors import CORS
from routes.recommend_routes import recommend_bp

app = Flask(__name__)

CORS(app)

app.register_blueprint(recommend_bp)

@app.route('/')
def home():

    return {
        "message": "Backend Running Successfully"
    }

if __name__ == '__main__':

    app.run(debug=True)