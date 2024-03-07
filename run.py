from flask import Flask
import g4f
import g4f.api

# Create a Flask application object
app = Flask(__name__)

# Route for the index page
@app.route('/')
def index():
    return 'Hello, World!'

if __name__ == "__main__":
    print(f'Starting server... [g4f v-{g4f.version.utils.current_version}]')

    # Run the Flask app using Gunicorn
    from gunicorn.app.base import BaseApplication

    class FlaskApplication(BaseApplication):
        def __init__(self, app, options=None):
            self.application = app
            self.options = options or {}
            super().__init__()

        def load_config(self):
            for key, value in self.options.items():
                self.cfg.set(key, value)

        def load(self):
            return self.application

    options = {
        'bind': '0.0.0.0:10000',  # Bind to all addresses on port 10000
        'workers': 4  # Number of worker processes
    }

    FlaskApplication(app, options).run()
