from flask import Flask, jsonify
import os


def create_app() -> Flask:
    app = Flask(__name__)

    @app.get("/")
    def index():
        return jsonify({
            "service": "devops-starter",
            "status": "running",
            "environment": os.getenv("APP_ENV", "dev")
        })

    @app.get("/health")
    def health():
        return jsonify({"status": "ok"}), 200

    @app.get("/info")
    def info():
        return jsonify({
            "version": os.getenv("APP_VERSION", "0.1.0"),
            "port": os.getenv("PORT", "8000")
        })

    return app


if __name__ == "__main__":
    port = int(os.getenv("PORT", "8000"))
    app = create_app()
    app.run(host="0.0.0.0", port=port)
