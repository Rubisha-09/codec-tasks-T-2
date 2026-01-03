from flask import Flask, request, jsonify
from parser import parse_resume

app = Flask(__name__)

@app.route("/")
def home():
    return "Resume Parser is running successfully!"

@app.route("/upload", methods=["POST"])
def upload_resume():
    file = request.files["resume"]
    file_path = "resume.pdf"
    file.save(file_path)

    name, skills = parse_resume(file_path)

    return jsonify({
        "Name": name,
        "Skills": skills
    })

if __name__ == "__main__":
    app.run(debug=True)
