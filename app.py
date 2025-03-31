# app.py

from flask import Flask
from faculty import faculty_bp

app = Flask(__name__)

# Register faculty blueprint
app.register_blueprint(faculty_bp)

@app.route("/", methods=["GET"])
def home():
    return {"message": "SRM Faculty API is running!"}

if __name__ == "__main__":
    app.run(debug=True)
