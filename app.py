from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({
        "message": "message": "Hello from GitHub PR validation",
        "ci_engine": "Azure DevOps Pipeline",
        "source_of_truth": "GitHub"
    })

@app.route("/health")
def health():
    return jsonify({"status": "healthy"}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
