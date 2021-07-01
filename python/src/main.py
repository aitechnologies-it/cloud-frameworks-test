from app import create_app

try:
    app = create_app()
except Exception as e:
    print("ERROR: could not create app.")
    raise e

if __name__ == "__main__":
    app.run(host="localhost", port=app.config.get('FLASK_PORT'), debug=app.config.get('DEBUG'))
