
@app.route("/")
def home():
    return jsonify({
        "message": "Welcome to Automatic Jenkins CI/CD Deployment!",
        "status": "Application Running",
        "project": "Jenkins Pipeline"
    })

@app.route("/health")
def health():
    return jsonify({
        "status": "healthy"
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
"message": "Welcome to Jenkins CI/CD Practice!",
